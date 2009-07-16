# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Layer(IRhinoScript):



    def add_layer(self, layer, color, visible, locked, parent):
        """

        Adds a new layer to the document.

        Parameters

        Layer : Optional, String, str, String
        Color : Optional, Number, lng, Integer
        Visible : Optional, Boolean, bln, Boolean
        Locked : Optional, Boolean, bln, Boolean
        Parent : Optional, String, str, String

        Returns

        String : The name of the new layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(3, 1, (12, 0), ((8, 0), (3, 0), (11, 0), (11, 0), (8, 0),), u'AddLayer', None, layer, color, visible, locked, parent)

    def current_layer(self, layer):
        """

        Returns or changes the current layer.

        Parameters

        Layer : Optional, String, str, String

        Returns

        String : If a layer name is not specified, the name of the current layer if successful.
        String : If a layer name is specified, the name of the previous current layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(5, 1, (12, 0), ((8, 0),), u'CurrentLayer', None, layer)

    def delete_layer(self, layer):
        """

        Removes an existing layer from the document.  The layer to be removed cannot be the current layer.  Unlike the PurgeLayer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.

        Parameters

        Layer : Required, String, str, String

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(4, 1, (12, 0), ((8, 0),), u'DeleteLayer', None, layer)

    def expand_layer(self, layer, expand):
        """

        Expands a layer. Expanded layers can be viewed in Rhino's Layer dialog.

        Parameters

        Layer : Required, String, str, String
        Expand : Required, Boolean, bln, Boolean

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(690, 1, (12, 0), ((8, 0), (11, 0),), u'ExpandLayer', None, layer, expand)

    def is_layer(self, layer):
        """

        Verifies the existence of a layer in the document.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(6, 1, (12, 0), ((8, 0),), u'IsLayer', None, layer)

    def is_layer_changeable(self, layer):
        """

        Verifies that the objects on a layer can be changed (normal).

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(18, 1, (12, 0), ((8, 0),), u'IsLayerChangeable', None, layer)

    def is_layer_child_of(self, layer, test):
        """

        Verifies that a layer is a child of another layer.

        Parameters

        Layer : Required, String, str, String
        Test : Required, String, str, String

        Returns

        Boolean : True if strTest is a child of strLayer. False otherwise.
        Null : On error.

        """

        return self._ApplyTypes_(692, 1, (12, 0), ((8, 0), (8, 0),), u'IsLayerChildOf', None, layer, test)

    def is_layer_current(self, layer):
        """

        Verifies that a layer is the current layer.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(313, 1, (12, 0), ((8, 0),), u'IsLayerCurrent', None, layer)

    def is_layer_empty(self, layer):
        """

        Verifies that an existing layer is empty, or contains no objects.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(7, 1, (12, 0), ((8, 0),), u'IsLayerEmpty', None, layer)

    def is_layer_expanded(self, layer):
        """

        Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's Layer dialog.

        Parameters

        Layer : Required, String, str, String

        Returns

        Boolean : True if expanded, False if collapsed.
        Null : On error.

        """

        return self._ApplyTypes_(689, 1, (12, 0), ((8, 0),), u'IsLayerExpanded', None, layer)

    def is_layer_locked(self, layer):
        """

        Verifies that an existing layer is locked.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(8, 1, (12, 0), ((8, 0),), u'IsLayerLocked', None, layer)

    def is_layer_on(self, layer):
        """

        Verifies that an existing layer is on.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(9, 1, (12, 0), ((8, 0),), u'IsLayerOn', None, layer)

    def is_layer_parent_of(self, layer, test):
        """

        Verifies that a layer is a parent of another layer.

        Parameters

        Layer : Required, String, str, String
        Test : Required, String, str, String

        Returns

        Boolean : True if strTest is a parent of strLayer. False otherwise.
        Null : On error.

        """

        return self._ApplyTypes_(693, 1, (12, 0), ((8, 0), (8, 0),), u'IsLayerParentOf', None, layer, test)

    def is_layer_reference(self, layer):
        """

        Verifies that an existing layer is from a reference file.

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(10, 1, (12, 0), ((8, 0),), u'IsLayerReference', None, layer)

    def is_layer_selectable(self, layer):
        """

        Verifies that an existing layer is selectable (normal and reference).

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(19, 1, (12, 0), ((8, 0),), u'IsLayerSelectable', None, layer)

    def is_layer_visible(self, layer):
        """

        Verifies that an existing layer is visible (normal, locked,  and reference).

        Parameters

        Layer : Required, String, str, String

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(20, 1, (12, 0), ((8, 0),), u'IsLayerVisible', None, layer)

    def layer_child_count(self, layer):
        """

        Returns the number of immediate child layers of a layer.

        Parameters

        Layer : Required, String, str, String

        Returns

        Number : The number of immediate child layers if successful
        Null : On error.

        """

        return self._ApplyTypes_(694, 1, (12, 0), ((8, 0),), u'LayerChildCount', None, layer)

    def layer_children(self, layer):
        """

        Returns the immediate child layers of a layer.

        Parameters

        Layer : Required, String, str, String

        Returns

        Array : An array of strings identifying the layer's children if successful
        Null : If the layer has no children, or on error.

        """

        return self._ApplyTypes_(691, 1, (12, 0), ((8, 0),), u'LayerChildren', None, layer)

    def layer_color(self, layer, color):
        """

        Returns or changes the color of a layer.  Layer colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        Layer : Required, String, str, String
        Color : Optional, Number, lng, Integer

        Returns

        Number : If a color value  is not specified,  the current color value if successful.
        Number : If a color value is specified, the previous color value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(11, 1, (12, 0), ((8, 0), (3, 0),), u'LayerColor', None, layer, color)

    def layer_count(self):
        """

        Returns the number of layers in the document.

        No parameters

        Returns

        Number : The number of layers in the document.

        """

        return self._ApplyTypes_(12, 1, (12, 0), (,), u'LayerCount', None, )

    def layer_linetype(self, layer, linetype):
        """

        Returns or changes the linetype of a layer.

        Parameters

        Layer : Required, String, str, String
        Linetype : Optional, String, str, String

        Returns

        String : If a linetype is not specified,  the name of the current linetype if successful.
        String : If a linetype is specified, the name of the previous linetype if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(602, 1, (12, 0), ((8, 0), (8, 0),), u'LayerLinetype', None, layer, linetype)

    def layer_locked(self, layer, visible):
        """

        Returns or changes the locked mode of a layer. This method should be use instead of LayerMode.

        Parameters

        Layer : Required, String, str, String
        Visible : Optional, Boolean, bln, Boolean

        Returns

        Boolean : If a layer mode is not specified,  the current layer locked mode if successful.
        Boolean : If a layer mode is specified, the previous layer locked mode if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(601, 1, (12, 0), ((8, 0), (11, 0),), u'LayerLocked', None, layer, visible)

    def layer_material_index(self, layer):
        """

        Returns the material index of a layer.  A material index of -1 indicates that no material has been assigned to the layer.  Thus, the layer will use Rhino's default layer material.

        Parameters

        Layer : Required, String, str, String

        Returns

        Number : A zero-based material index if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(13, 1, (12, 0), ((8, 0),), u'LayerMaterialIndex', None, layer)

    def layer_mode(self, layer, mode):
        """

        Returns or changes the mode of a layer.

        Parameters

        Layer : Required, String, str, String
        Mode : Optional, Number, int, Integer

        Returns

        Number : If a layer mode is not specified,  the current layer mode  if successful.
        Number : If a layer mode is specified, the previous layer mode if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(14, 1, (12, 0), ((8, 0), (2, 0),), u'LayerMode', None, layer, mode)

    def layer_names(self, sort):
        """

        Returns the names of all layers in the document.

        Parameters

        Sort : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of layer names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(15, 1, (12, 0), ((11, 0),), u'LayerNames', None, sort)

    def layer_order(self, layer):
        """

        Returns the current display order index of a layer as displayed in Rhino's Layer dialog box.  A display order index of -1 indicates that the current Layer dialog filter does not allow the layer to appear in the layer list.

        Parameters

        Layer : Required, String, str, String

        Returns

        Number : A zero-based display order index if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(17, 1, (12, 0), ((8, 0),), u'LayerOrder', None, layer)

    def layer_print_color(self, layer, color):
        """

        Returns or changes the print color of a layer. Layer print colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be printed.

        Parameters

        Layer : Required, String, str, String
        Color : Optional, Number, lng, Integer

        Returns

        Number : If a layer print color is not specified,  the current layer print color if successful.
        Number : If a layer print color is specified, the previous layer print color if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(603, 1, (12, 0), ((8, 0), (3, 0),), u'LayerPrintColor', None, layer, color)

    def layer_print_width(self, layer, width):
        """

        Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.

        Parameters

        Layer : Required, String, str, String
        Width : Optional, Number, dbl, Double

        Returns

        Number : If a layer print width is not specified,  the current layer print width if successful.
        Number : If a layer print width is specified, the previous layer print width if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(604, 1, (12, 0), ((8, 0), (5, 0),), u'LayerPrintWidth', None, layer, width)

    def layer_visible(self, layer, visible):
        """

        Returns or changes the visibility property of a layer. This method should be use instead of LayerMode.

        Parameters

        Layer : Required, String, str, String
        Visible : Optional, Boolean, bln, Boolean

        Returns

        Boolean : If a layer mode is not specified,  the current layer visibility if successful.
        Boolean : If a layer mode is specified, the previous layer visibility if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(600, 1, (12, 0), ((8, 0), (11, 0),), u'LayerVisible', None, layer, visible)

    def parent_layer(self, layer, parent):
        """

        Returns or modifies the parent layer of a layer.

        Parameters

        Layer : Required, String, str, String
        Parent : Optional, String, str, String

        Returns

        String : If strParent is not specified, the name of the current parent layer if successful.
        String : If strParent is specified, the name of the previous parent layer if successful.
        Null : If the layer does not have a parent, or on error.

        """

        return self._ApplyTypes_(688, 1, (12, 0), ((8, 0), (8, 0),), u'ParentLayer', None, layer, parent)

    def purge_layer(self, layer):
        """

        Removes an existing layer from the document.  Unlike the DeleteLayer method, PurgeLayer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.

        Parameters

        Layer : Required, String, str, String

        Returns

        String : The name of the purged layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(291, 1, (12, 0), ((8, 0),), u'PurgeLayer', None, layer)

    def rename_layer(self, old_name, new_name):
        """

        Renames an existing layer.

        Parameters

        OldName : Required, String, str, String
        NewName : Required, String, str, String

        Returns

        String : The new layer name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(16, 1, (12, 0), ((8, 0), (8, 0),), u'RenameLayer', None, old_name, new_name)

