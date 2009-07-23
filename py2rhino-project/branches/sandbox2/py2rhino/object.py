# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Object(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_object_mesh(self, object, quality=None, enable=None):
        """        
        Adds custom render mesh parameters to a meshable object, such as a surface or a polysurface.  If an object has custom render mesh parameters and they are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a meshable object.
            
        quality, Integer, Optional        
        The initial settings of the new custom render mesh parameters. The available options are as follows:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
            
        enable, Boolean, Optional        
        Enable the custom render mesh parameters.  If omitted, the newly added parameters will be enabled (True).
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current enabled/disabled state if successful.

        boolean
        If blnEnable is not specified, then the current enabled/disabled state if successful.

        null
        If the object does not have custom render mesh parameters, or on error.

        """

        params = [object, quality, enable]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1)]
        flattened = [object, quality, enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(866, 1, (VT_VARIANT, 0), magic, u"AddObjectMesh", None, *flattened)

    def box_morph_object(self, objects, box_points, copy=None):
        """        
        Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to morph.
            
        box_points, Array of ????, Required        
        An array of eight 3-D points that contain the modified bounding box points.
            
        copy, Boolean, Optional        
        Copy the object. If omitted, the object will not be copied (False).
            
        Returns
        =======

        string
        The identifier of the morphed object if successful.

        array
        An array of strings identifying the morphed objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, box_points, copy]
        required = [True, True, False]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(box_points), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(918, 1, (VT_VARIANT, 0), magic, u"BoxMorphObject", None, *flattened)

    def copy_objects(self, objects, start=None, end=None):
        """        
        Copies one or more objects from one location to another, or in-place.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to copy.
            
        start, Array of ????, Optional        
        The 3-D starting, or base, point of the copy operation.  If omitted, the objects are copied in-place.
            
        end, Array of ????, Optional        
        The 3-D ending point of the copy operation.
            
        Returns
        =======

        array
        An array of strings identifying the copied objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, start, end]
        required = [True, False, False]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(objects), flatten_params(start), flatten_params(end)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(295, 1, (VT_VARIANT, 0), magic, u"CopyObjects", None, *flattened)

    def copy_objects_2(self, translation=None):
        """        
        Copies one or more objects from one location to another, or in-place.
    
        Parameters
        ==========

        translation, Array of ????, Optional        
        The 3-D translation vector.
            
        Returns
        =======

        array
        An array of strings identifying the copied objects if successful.

        null
        If not successful, or on error.

        """

        params = [translation]
        required = [False]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(translation)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(295, 1, (VT_VARIANT, 0), magic, u"CopyObjects", None, *flattened)

    def delete_objects(self, objects):
        """        
        Deletes one or more objects from the document.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to delete.
            
        Returns
        =======

        number
        The number of objects deleted if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(186, 1, (VT_VARIANT, 0), magic, u"DeleteObjects", None, *flattened)

    def enable_object_mesh(self, objects, enable=None):
        """        
        Enables or disables an object's custom render mesh parameters. If an object's custom render mesh parameters are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        The identifier of a meshable object.
            
        enable, Boolean, Optional        
        Enable the custom render mesh settings.
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current enabled/disabled state if successful.

        boolean
        If blnEnable is not specified, then the current enabled/disabled state if successful.

        null
        If the object does not have custom render mesh parameters, or on error.

        """

        params = [objects, enable]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(856, 1, (VT_VARIANT, 0), magic, u"EnableObjectMesh", None, *flattened)

    def flash_object(self, objects, style=None):
        """        
        Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        The identifiers of the objects to flash.
            
        style, Boolean, Optional        
        The flash style.  If True (default), then the objects will flash between their object color and Rhino's selected object color.  If false, then the objects will flash between invisible and visible.
            
        No returns


        """

        params = [objects, style]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), style]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(869, 1, (VT_VARIANT, 0), magic, u"FlashObject", None, *flattened)

    def hide_objects(self, objects):
        """        
        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to hide.
            
        Returns
        =======

        number
        The number of objects hidden if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(303, 1, (VT_VARIANT, 0), magic, u"HideObjects", None, *flattened)

    def is_layout_object(self, object):
        """        
        Verifies that an object is in either page layout space or model space.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(919, 1, (VT_VARIANT, 0), magic, u"IsLayoutObject", None, *flattened)

    def is_object(self, object):
        """        
        Verifies the existence of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        No returns


        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(46, 1, (VT_VARIANT, 0), magic, u"IsObject", None, *flattened)

    def is_object_hidden(self, object):
        """        
        Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(47, 1, (VT_VARIANT, 0), magic, u"IsObjectHidden", None, *flattened)

    def is_object_in_box(self, object, box, mode=None):
        """        
        Verifies an object's bounding box is inside of another bounding box.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        box, Array of Doubles, Required        
        The bounding box to test against. A bounding box is an array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
            
        mode, Boolean, Optional        
        The test mode.
		Value
		Description
		True (Default)
		The object's bounding box must be contained by the test bounding box. In other words, test.min <= object.min and object.max <= test.max.
		False
            
        Returns
        =======

        null
        On error.

        """

        params = [object, box, mode]
        required = [True, True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [object, flatten_params(box), mode]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(799, 1, (VT_VARIANT, 0), magic, u"IsObjectInBox", None, *flattened)

    def is_object_in_group(self, object, group=None):
        """        
        Verifies that an object is a member of a specified group.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        group, String, Optional        
        The name of a group.  If omitted, the function verifies that the object is a member of any group.
            
        Returns
        =======

        null
        On error.

        """

        params = [object, group]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(188, 1, (VT_VARIANT, 0), magic, u"IsObjectInGroup", None, *flattened)

    def is_object_locked(self, object):
        """        
        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(48, 1, (VT_VARIANT, 0), magic, u"IsObjectLocked", None, *flattened)

    def is_object_normal(self, object):
        """        
        Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(49, 1, (VT_VARIANT, 0), magic, u"IsObjectNormal", None, *flattened)

    def is_object_reference(self, object):
        """        
        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(271, 1, (VT_VARIANT, 0), magic, u"IsObjectReference", None, *flattened)

    def is_object_selectable(self, object):
        """        
        Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(307, 1, (VT_VARIANT, 0), magic, u"IsObjectSelectable", None, *flattened)

    def is_object_selected(self, object):
        """        
        Verifies that an object is currently selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(50, 1, (VT_VARIANT, 0), magic, u"IsObjectSelected", None, *flattened)

    def is_object_solid(self, object):
        """        
        Verifies that an object is a closed, solid object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(189, 1, (VT_VARIANT, 0), magic, u"IsObjectSolid", None, *flattened)

    def is_object_valid(self, object):
        """        
        Verifies that an object's geometry is valid and without error.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        Returns
        =======

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(522, 1, (VT_VARIANT, 0), magic, u"IsObjectValid", None, *flattened)

    def is_visible_in_view(self, object, view=None):
        """        
        Verifies that an object is visible in a view.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object.
            
        view, String, Optional        
        The title of the view.  If omitted, the current active view is used.
            
        Returns
        =======

        null
        On error.

        """

        params = [object, view]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, view]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(727, 1, (VT_VARIANT, 0), magic, u"IsVisibleInView", None, *flattened)

    def lock_objects(self, objects):
        """        
        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to lock.
            
        Returns
        =======

        number
        The number of objects locked if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(304, 1, (VT_VARIANT, 0), magic, u"LockObjects", None, *flattened)

    def match_object_attributes(self, targets, source=None):
        """        
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    
        Parameters
        ==========

        targets, Array of ????, Required        
        An array of strings identifying the target objects.
            
        source, String, Optional        
        The identifier of the source object.  If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
            
        Returns
        =======

        number
        The number of objects whose attributes were modified if successful.

        null
        If not successful, or on error.

        """

        params = [targets, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(targets), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(781, 1, (VT_VARIANT, 0), magic, u"MatchObjectAttributes", None, *flattened)

    def mirror_objects(self, objects, start_pt, end_pt, copy=None):
        """        
        Mirrors one or more objects.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to mirror.
            
        start_pt, Array of Doubles, Required        
        The start of the mirror plane.
            
        end_pt, Array of Doubles, Required        
        The end of the mirror plane.
            
        copy, Boolean, Optional        
        Copy the objects. If omitted, the objects will not be copied (False).
            
        Returns
        =======

        string
        An array of strings identifying the mirrored objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, start_pt, end_pt, copy]
        required = [True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(start_pt), flatten_params(end_pt), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(590, 1, (VT_VARIANT, 0), magic, u"MirrorObjects", None, *flattened)

    def move_objects(self, objects, start, end):
        """        
        Copies one or more objects.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to move.
            
        start, Array of ????, Required        
        The 3-D starting, or base, point of the move operation.
            
        end, Array of ????, Required        
        The 3-D ending point of the move operation.
            
        Returns
        =======

        number
        An array of strings identifying the moved objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, start, end]
        required = [True, True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(objects), flatten_params(start), flatten_params(end)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(296, 1, (VT_VARIANT, 0), magic, u"MoveObjects", None, *flattened)

    def move_objects_2(self, translation):
        """        
        Copies one or more objects.
    
        Parameters
        ==========

        translation, Array of ????, Required        
        The 3-D translation vector.
            
        Returns
        =======

        number
        An array of strings identifying the moved objects if successful.

        null
        If not successful, or on error.

        """

        params = [translation]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(translation)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(296, 1, (VT_VARIANT, 0), magic, u"MoveObjects", None, *flattened)

    def object_color(self, objects, color=None):
        """        
        Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        color, Integer, Optional        
        The new color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.
            
        Returns
        =======

        number
        If a color value is not specified,  the current color value if successful.

        number
        If a color value is specified, the previous color value if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, color]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I4, 1)]
        flattened = [flatten_params(objects), color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(191, 1, (VT_VARIANT, 0), magic, u"ObjectColor", None, *flattened)

    def object_color_source(self, objects, source=None):
        """        
        Returns or modifies the color source of an object.   The color used to display objects is specified in one of four ways:
		1. Color from layer.  The object's layer determines the object's color.
		2. Color from object.  The object's color is set by the object itself.
		3. Color from material.  The object's diffuse material color determines the object's color.
		4. Color from parent. For objects with parents, like objects in block instances, use parent's color source. If no parent, treats as color from layer.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        source, Integer, Optional        
        The new color source.  If omitted, the current color source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Color from layer
		1
		Color from object
		2
		Color from material
		3
            
        Returns
        =======

        number
        If a color source is not specified,  the current color source if successful.

        number
        If a color source is specified, the previous color source if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(192, 1, (VT_VARIANT, 0), magic, u"ObjectColorSource", None, *flattened)

    def object_description(self, object):
        """        
        Returns a short text description of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        string
        A short text description of the object is successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(470, 1, (VT_VARIANT, 0), magic, u"ObjectDescription", None, *flattened)

    def object_dump(self, object, type=None):
        """        
        Returns a detailed description of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        type, Integer, Optional        
        The acceptable values are as follows:
		Value
		Description
		0 (Default)
		Returns both geometry and attribute details. This is equivalent to the results of the What command.
		1
		Returns geometry details.
		2
		Returns attribute details.
		3
            
        Returns
        =======

        string
        A detailed description of the object is successful.

        null
        If not successful, or on error.

        """

        params = [object, type]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [object, type]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(705, 1, (VT_VARIANT, 0), magic, u"ObjectDump", None, *flattened)

    def object_groups(self, object):
        """        
        Returns all of the group names that an object is assigned.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        array
        An array of all group names for the object if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(193, 1, (VT_VARIANT, 0), magic, u"ObjectGroups", None, *flattened)

    def object_has_mesh(self, object):
        """        
        Verifies that an object has custom render mesh parameters.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a meshable object.
            
        Returns
        =======

        boolean
        True of the object has custom render mesh parameters, False otherwise.

        null
        On error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(867, 1, (VT_VARIANT, 0), magic, u"ObjectHasMesh", None, *flattened)

    def object_layer(self, objects, layer=None):
        """        
        Returns or modifies the layer of an object.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        layer, String, Optional        
        The name of an existing layer.  If omitted, the current object layer is returned.  Note, if arrObjects is specified, strLayer is required.
            
        Returns
        =======

        number
        If a layer is not specified,  the object's current layer if successful.

        number
        If a layer is specified, the object's previous layer if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, layer]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(objects), layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(51, 1, (VT_VARIANT, 0), magic, u"ObjectLayer", None, *flattened)

    def object_layout(self, object, layout=None, return_name=None):
        """        
        Returns or changes the layout or model space of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        layout, String, Optional        
        To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view. To move an object from page layout space to model space, just specify Null.
            
        return_name, Boolean, Optional        
        If True (default), then the name, or title, of the page layout view is returned. If False, then the identifier of the page layout view is returned.
            
        Returns
        =======

        string
        If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.

        string
        If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.

        null
        If not successful, or on error.

        """

        params = [object, layout, return_name]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [object, layout, return_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(924, 1, (VT_VARIANT, 0), magic, u"ObjectLayout", None, *flattened)

    def object_linetype(self, objects, layer=None):
        """        
        Returns or modifies the linetype of an object.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        layer, String, Optional        
        The name of an existing linetype.  If omitted, the current object linetype is returned.  Note, if arrObjects is specified, strLinetype is required.
            
        Returns
        =======

        number
        If a linetype is not specified,  the object's current linetype if successful.

        number
        If a linetype is specified, the object's previous linetype if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, layer]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(objects), layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(646, 1, (VT_VARIANT, 0), magic, u"ObjectLinetype", None, *flattened)

    def object_linetype_source(self, objects, source=None):
        """        
        Returns or modifies the linetype source of an object.   The linetype used to display objects is specified in one of three ways:
		1. Linetype from layer.  The object's layer determines the object's linetype.
		2. Linetype from object. The object's linetype is set by the object itself.
		3. Linetype from parent.  For objects with parents, like objects in block instances, use parent's linetype. If no parent, treats as linetype from layer.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        source, Integer, Optional        
        The new linetype source.  If omitted, the current linetype source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Layer.  Use the object's layer linetype.
		1
		Object.  Use the object's linetype.
		2
		<unused>
		3
            
        Returns
        =======

        number
        If a linetype source is not specified,  the current linetype source if successful.

        number
        If a linetype source is specified, the previous linetype source if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(647, 1, (VT_VARIANT, 0), magic, u"ObjectLinetypeSource", None, *flattened)

    def object_material_index(self, object):
        """        
        Returns the material index of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The rendering material index if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(194, 1, (VT_VARIANT, 0), magic, u"ObjectMaterialIndex", None, *flattened)

    def object_material_source(self, objects, source=None):
        """        
        Returns or modifies the rendering material source of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		The index of the render material used to render an object is specified in one of three ways:
		1. Material from layer.  The rendering material assigned to the layer is used.
		2. Material from object.  The rendering material assigned to the object is used.
		3. Material from parent.  For objects with parents, like objects in block instances, use parent's material. If no parent, treats as material from layer.
		The default rendering material source for new objects is "material by layer."
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        source, Integer, Optional        
        The new rendering material source.  If omitted, the current material source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Material from layer
		1
		Material from object
		2
		<unused>
		3
            
        Returns
        =======

        number
        If a rendering material source is not specified,  the current rendering material source if successful.

        number
        If a rendering material source is specified, the previous rendering material source if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(195, 1, (VT_VARIANT, 0), magic, u"ObjectMaterialSource", None, *flattened)

    def object_mesh_density(self, object, density=None):
        """        
        Returns or modifies an object's custom render mesh parameter's mesh density property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        density, Double, Optional        
        The render mesh density, which is a number between 0.0 and 1.0.
            
        Returns
        =======

        boolean
        If dblDensity is not specified, the current render mesh density if successful.

        boolean
        If dblDensity is specified, the previous render mesh density if successful.

        null
        If not successful, or on error.

        """

        params = [object, density]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, density]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(858, 1, (VT_VARIANT, 0), magic, u"ObjectMeshDensity", None, *flattened)

    def object_mesh_max_angle(self, object, angle=None):
        """        
        Returns or modifies an object's custom render mesh parameter's maximum angle property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        angle, Double, Optional        
        The render mesh maximum angle in degrees.
            
        Returns
        =======

        boolean
        If dblAngle is not specified, the current render mesh maximum angle if successful.

        boolean
        If dblAngle is specified, the previous render mesh maximum angle if successful.

        null
        If not successful, or on error.

        """

        params = [object, angle]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, angle]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(859, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxAngle", None, *flattened)

    def object_mesh_max_aspect_ratio(self, object, ratio=None):
        """        
        Returns or modifies an object's custom render mesh parameter's maximum aspect ratio property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        ratio, Double, Optional        
        The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.
            
        Returns
        =======

        boolean
        If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.

        boolean
        If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.

        null
        If not successful, or on error.

        """

        params = [object, ratio]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, ratio]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(860, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxAspectRatio", None, *flattened)

    def object_mesh_max_dist_edge_to_srf(self, object, distance=None):
        """        
        Returns or modifies an object's custom render mesh parameter's maximum distance, edge to surface property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        distance, Double, Optional        
        The render mesh maximum distance, edge to surface.
            
        Returns
        =======

        boolean
        If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.

        boolean
        If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.

        null
        If not successful, or on error.

        """

        params = [object, distance]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, distance]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(863, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxDistEdgeToSrf", None, *flattened)

    def object_mesh_max_edge_length(self, object, length=None):
        """        
        Returns or modifies an object's custom render mesh parameter's maximum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        length, Double, Optional        
        The render mesh maximum edge length.
            
        Returns
        =======

        boolean
        If dblLength is not specified, the current render mesh maximum edge length if successful.

        boolean
        If dblLength is specified, the previous render mesh maximum edge length if successful.

        null
        If not successful, or on error.

        """

        params = [object, length]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, length]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(862, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxEdgeLength", None, *flattened)

    def object_mesh_min_edge_length(self, object, length=None):
        """        
        Returns or modifies an object's custom render mesh parameter's minimum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        length, Double, Optional        
        The render mesh minimum edge length.
            
        Returns
        =======

        boolean
        If dblLength is not specified, the current render mesh minimum edge length if successful.

        boolean
        If dblLength is specified, the previous render mesh minimum edge length if successful.

        null
        If not successful, or on error.

        """

        params = [object, length]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, length]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(861, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMinEdgeLength", None, *flattened)

    def object_mesh_min_initial_grid_quads(self, object, quads=None):
        """        
        Returns or modifies an object's custom render mesh parameter's minimum initial grid quads property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        quads, Integer, Optional        
        The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.
            
        Returns
        =======

        boolean
        If intQuads is not specified, the current render mesh minimum initial grid quads if successful.

        boolean
        If intQuads is specified, the previous render mesh minimum initial grid quads if successful.

        null
        If not successful, or on error.

        """

        params = [object, quads]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [object, quads]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(864, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMinInitialGridQuads", None, *flattened)

    def object_mesh_quality(self, object, quality=None):
        """        
        Returns or sets the render mesh quality of an object's custom render mesh parameters.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        quality, Integer, Optional        
        The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
            
        Returns
        =======

        boolean
        If intQuality is not specified, the current render mesh quality if successful.

        boolean
        If intQuality is specified, the previous render mesh quality if successful.

        null
        If the object does not have custom render mesh parameters, or on error.

        """

        params = [object, quality]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [object, quality]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(857, 1, (VT_VARIANT, 0), magic, u"ObjectMeshQuality", None, *flattened)

    def object_mesh_settings(self, object, settings=None):
        """        
        Returns or sets the render mesh settings of an object's custom render mesh parameters.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an object that has custom render mesh parameters.
            
        settings, Integer, Optional        
        The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 15.  The bit values are as follows:
		Value
		Description
		0
		No settings enabled.
		1
		Refine mesh enabled.
		2
		Jagged seams enabled.
		4
		Simple planes enabled.
		8
            
        Returns
        =======

        boolean
        If intSettings is not specified, the current render mesh settings if successful.

        boolean
        If intSettings is specified, the previous render mesh settings if successful.

        null
        If the object does not have custom render mesh parameters, or on error.

        """

        params = [object, settings]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [object, settings]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(865, 1, (VT_VARIANT, 0), magic, u"ObjectMeshSettings", None, *flattened)

    def object_names(self, objects, names=None):
        """        
        Returns or modifies the user-definable name of one or more objects.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects.
            
        names, Array of Strings, Optional        
        An array of strings identifying the new user-definable names. This array must have the same upper bounds as arrObjects.  Each element in arrNames will correspond with each element in arrObjects.
            
        Returns
        =======

        array
        If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.

        array
        If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.

        null
        If not successful, or on error.

        """

        params = [objects, names]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(objects), flatten_params(names)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(639, 1, (VT_VARIANT, 0), magic, u"ObjectNames", None, *flattened)

    def object_print_color(self, objects, color=None):
        """        
        Returns or modifies the print color of an object.  Object print colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        color, Integer, Optional        
        The new print color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.
            
        Returns
        =======

        number
        If a print color value is not specified,  the current print color value if successful.

        number
        If a print color value is specified, the previous print color value if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, color]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I4, 1)]
        flattened = [flatten_params(objects), color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(805, 1, (VT_VARIANT, 0), magic, u"ObjectPrintColor", None, *flattened)

    def object_print_color_source(self, objects, source=None):
        """        
        Returns or modifies the print color source of an object.  The color used to print objects is specified in one of four ways:
		1. Print color from layer.  Use the print color assigned to the object's layer.
		2. Print color from object.  Use the print color that is assigned to the object.
		3. Print color from display.  Use the object's display color.
		4. Print color from parent.  For objects with parents, like objects in block instances, use parent's print color.  If no parent, treats as print color from layer.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        source, Integer, Optional        
        The new print color source.  If omitted, the current print color source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Print color by layer.
		1
		Print color by object.
		2
		Print color by display.
		3
            
        Returns
        =======

        number
        If a print color source is not specified,  the current color source if successful.

        number
        If a print color source is specified, the previous color source if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(806, 1, (VT_VARIANT, 0), magic, u"ObjectPrintColorSource", None, *flattened)

    def object_print_width(self, objects, width=None):
        """        
        Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        width, Double, Optional        
        The new print width value in millimeters, where dblWidth = 0.0 means use the default width, and dblWidth < 0.0 means do not print (visible for screen display, but does not show on print).  If omitted, the current object print width is returned.  Note, if arrObjects is specified, dblWidth is required.
            
        Returns
        =======

        number
        If a print width value is not specified,  the current print width value if successful.

        number
        If a print width value is specified, the previous print width value if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, width]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_R8, 1)]
        flattened = [flatten_params(objects), width]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(807, 1, (VT_VARIANT, 0), magic, u"ObjectPrintWidth", None, *flattened)

    def object_print_width_source(self, objects, source=None):
        """        
        Returns or modifies the print width source of an object.  The width used to print objects is specified in one of three ways:
		1. Print width from layer.  Use the print width assigned to the object's layer.
		2. Print width from object.  Use the print width that is assigned to the object.
		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        source, Integer, Optional        
        The new print width source.  If omitted, the current print width source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Print width by layer.
		1
		Print width by object.
		2
		<unused>
		3
            
        Returns
        =======

        number
        If a print width source is not specified,  the current width source if successful.

        number
        If a print width source is specified, the previous width source if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, source]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), source]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(808, 1, (VT_VARIANT, 0), magic, u"ObjectPrintWidthSource", None, *flattened)

    def object_top_group(self, object):
        """        
        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        string
        The top most group name of the object if successful

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(197, 1, (VT_VARIANT, 0), magic, u"ObjectTopGroup", None, *flattened)

    def object_type(self, object):
        """        
        Returns the object type.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The object type if successful.  The valid object types are as follows:

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(198, 1, (VT_VARIANT, 0), magic, u"ObjectType", None, *flattened)

    def object_u_r_l(self, objects, u_r_l=None):
        """        
        Returns or modifies the user-definable URL of an object.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to modify.
            
        u_r_l, String, Optional        
        The new object URL.  If omitted, the current object URL is returned.  Note, if arrObjects is specified, strURL is required.
            
        Returns
        =======

        string
        If an object URL is not specified,  the current object URL if successful.

        string
        If an object URL is specified,  the previous object URL if successful.

        number
        If arrObjects is specified, then the number of objects modified if successful.

        null
        If not successful, or on error.

        """

        params = [objects, u_r_l]
        required = [True, False]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(objects), u_r_l]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(199, 1, (VT_VARIANT, 0), magic, u"ObjectURL", None, *flattened)

    def orient_objects(self, objects, reference, target, flags=None):
        """        
        Orients one or more objects based on input points.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to orient.
            
        reference, Array of Doubles, Required        
        An array of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            
        target, Array of Doubles, Required        
        An array of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            
        flags, Integer, Optional        
        The orient flags.  Values can be added together to specify multiple options.
		Value
		Description
		1
		Copy object.  The default is not to copy the objects.
		2
            
        Returns
        =======

        array
        An array of strings identifying the oriented objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, reference, target, flags]
        required = [True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1)]
        flattened = [flatten_params(objects), flatten_params(reference), flatten_params(target), flags]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(391, 1, (VT_VARIANT, 0), magic, u"OrientObjects", None, *flattened)

    def remap_objects(self, object, src_plane, dst_plane, copy=None):
        """        
        Remqps one or more objects from one plane, or coordinate system, to another.
    
        Parameters
        ==========

        object, Array of Strings, Required        
        The identifiers of the objects to remap.
            
        src_plane, Array of Doubles, Required        
        The source plane to transform from.
            
        dst_plane, Array of Doubles, Required        
        The destination plane to transform to.
            
        copy, Boolean, Optional        
        Copy the object. If omitted, the object will not be copied (False).
            
        Returns
        =======

        array
        An array of strings identifying the remapped objects if successful.

        null
        If not successful, or on error.

        """

        params = [object, src_plane, dst_plane, copy]
        required = [True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(object), flatten_params(src_plane), flatten_params(dst_plane), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(656, 1, (VT_VARIANT, 0), magic, u"RemapObjects", None, *flattened)

    def rotate_objects(self, objects, point, angle, axis=None, copy=None):
        """        
        Rotates one or more objects. Rotation is based on the active construction plane.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to rotate.
            
        point, Array of Doubles, Required        
        The 3-D center point of the rotation.
            
        angle, Double, Required        
        The rotation angle in degrees.
            
        axis, Array of Doubles, Optional        
        A 3-D vector that identifies the axis of rotation. If omitted, the Z axis of the active construction plane is used as the rotation axis.
            
        copy, Boolean, Optional        
        Copy the object. If omitted, the objects will not be copied (False).
            
        Returns
        =======

        string
        An array of strings identifying the rotated objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, point, angle, axis, copy]
        required = [True, True, True, False, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(point), angle, flatten_params(axis), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(393, 1, (VT_VARIANT, 0), magic, u"RotateObjects", None, *flattened)

    def scale_objects(self, objects, origin, scale, copy=None):
        """        
        Scales one or more objects. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to scale.
            
        origin, Array of Doubles, Required        
        The origin of the scale transformation.
            
        scale, Array of Doubles, Required        
        An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply. Scaling is based on the active construction plane.
            
        copy, Boolean, Optional        
        Copy the objects. If omitted, the objects will not be copied (False).
            
        Returns
        =======

        array
        An array of strings identifying the scaled objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, origin, scale, copy]
        required = [True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(origin), flatten_params(scale), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(586, 1, (VT_VARIANT, 0), magic, u"ScaleObjects", None, *flattened)

    def select_objects(self, objects):
        """        
        Selects one or more objects.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to select.
            
        Returns
        =======

        number
        The number of objects selected if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(298, 1, (VT_VARIANT, 0), magic, u"SelectObjects", None, *flattened)

    def shear_objects(self, objects, origin, ref_pt, scale, copy=None):
        """        
        Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to shear.
            
        origin, Array of Doubles, Required        
        The origin of the shear transformation.
            
        ref_pt, Array of Doubles, Required        
        The reference point of the shear transformation.
            
        scale, Array of Integers, Required        
        An angle in degrees of the shear transformation, where -90.0 <= angle <= 90.0.
            
        copy, Boolean, Optional        
        Copy the objects. If omitted, the objects will not be copied (False).
            
        Returns
        =======

        array
        An array of strings identifying the scaled objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, origin, ref_pt, scale, copy]
        required = [True, True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(origin), flatten_params(ref_pt), flatten_params(scale), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(588, 1, (VT_VARIANT, 0), magic, u"ShearObjects", None, *flattened)

    def show_objects(self, objects):
        """        
        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to show.
            
        Returns
        =======

        number
        The number of objects shown if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(305, 1, (VT_VARIANT, 0), magic, u"ShowObjects", None, *flattened)

    def transform_objects(self, objects, matrix, copy=None):
        """        
        Moves, scales, or rotates one or more objects given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1
		0
		0
		dX
		0
		1
		0
		dY
		0
		0
		1
		dZ
		0
		0
		0
		1
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings identifying the objects to transform.
            
        matrix, Array of ????, Required        
        The transformation matrix (4x4 array of numbers).
            
        copy, Boolean, Optional        
        Copy the objects. If omitted, the objects will not be copied (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly transformed objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, matrix, copy]
        required = [True, True, False]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), flatten_params(matrix), copy]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(302, 1, (VT_VARIANT, 0), magic, u"TransformObjects", None, *flattened)

    def unlock_objects(self, objects):
        """        
        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to unlock.
            
        Returns
        =======

        number
        The number of objects unlocked if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(306, 1, (VT_VARIANT, 0), magic, u"UnlockObjects", None, *flattened)

    def unselect_objects(self, objects):
        """        
        Unselects one or more selected objects.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
        An array of strings identifying the objects to unselect.
            
        Returns
        =======

        number
        The number of objects unselected if successful.

        null
        If not successful, or on error.

        """

        params = [objects]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(objects)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(300, 1, (VT_VARIANT, 0), magic, u"UnselectObjects", None, *flattened)

