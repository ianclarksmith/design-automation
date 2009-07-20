# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Selection(IRhinoScript):



    def all_objects(self, select, include_lights, include_grips):
        """        
        Returns the identifiers of all objects in the document.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(30, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"AllObjects", None, select, include_lights, include_grips)

    def first_object(self, select, include_lights, include_grips):
        """        
        Returns the identifier of the first object in the document.  The first object in the document is the last object created by the user.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the object.  If omitted, the object is not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        string
        The identifier of the object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(31, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"FirstObject", None, select, include_lights, include_grips)

    def get_curve_object(self, message, pre_select, select):
        """        
        Prompts the user to pick, or select, a single curve object.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Select the picked objects.  If omitted, the objects that are picked are not selected (False).
            
        Returns
        =======

        array
        An array of selection information if successful. The array will contain the following information:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(575, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"GetCurveObject", None, message, pre_select, select)

    def get_object(self, message, type, pre_select, select, objects):
        """        
        Prompts the user to pick, or select, a single object.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        type, Integer, Optional        
        The type or types of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects (default)
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
            
        objects, Array of ????, Optional        
        An array of strings identifying the objects that are allowed to be selected.
            
        Returns
        =======

        string
        The identifier of the picked object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(32, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1)), u"GetObject", None, message, type, pre_select, select, flatten(objects))

    def get_object_ex(self, message, type, pre_select, select, objects):
        """        
        Prompts the user to pick, or select, a single object.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        type, Integer, Optional        
        The type or types of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects (default)
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
            
        objects, Array of ????, Optional        
        An array of strings identifying the objects that are allowed to be selected.
            
        Returns
        =======

        array
        An array of selection information if successful. The array will contain the following information:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(819, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1)), u"GetObjectEx", None, message, type, pre_select, select, flatten(objects))

    def get_objects(self, message, type, group, pre_select, select, objects):
        """        
        Prompts the user to pick or select one or more objects.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        type, Integer, Optional        
        The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects (default)
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            
        group, Boolean, Optional        
        Honor object grouping.  If omitted and the user picks a group, the entire group will be picked (True). Note, if intType is set to a value other than 0 (All objects), then group selection will be disabled.
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
            
        objects, Array of ????, Optional        
        An array of strings identifying the objects that are allowed to be selected.
            
        Returns
        =======

        array
        An array of strings identifying the picked objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(33, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1)), u"GetObjects", None, message, type, group, pre_select, select, flatten(objects))

    def get_objects_ex(self, message, type, group, pre_select, select, objects):
        """        
        Prompts the user to pick or select one or more objects.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        type, Integer, Optional        
        The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects (default)
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            
        group, Boolean, Optional        
        Honor object grouping.  If omitted and the user picks a group, the entire group will be picked (True). Note, if intType is set to a value other than 0 (All objects), then group selection will be disabled.
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
            
        objects, Array of ????, Optional        
        An array of strings identifying the objects that are allowed to be selected.
            
        Returns
        =======

        array
        An array that contains arrays of selection information if successful. The array of selection information will contain the following:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(820, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1)), u"GetObjectsEx", None, message, type, group, pre_select, select, flatten(objects))

    def get_point_coordinates(self, message, pre_select):
        """        
        Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        Returns
        =======

        array
        An array of 3-D points, one for each selected point object, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(645, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"GetPointCoordinates", None, message, pre_select)

    def get_surface_object(self, message, pre_select, select):
        """        
        Prompts the user to pick, or select, a single surface object.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        pre_select, Boolean, Optional        
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            
        select, Boolean, Optional        
        Select the picked objects.  If omitted, the objects that are picked are not selected (False).
            
        Returns
        =======

        array
        An array of selection information if successful. The array will contain the following information:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(576, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"GetSurfaceObject", None, message, pre_select, select)

    def hidden_objects(self, include_lights, include_grips):
        """        
        Returns the identifiers of all hidden objects in the document.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(366, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"HiddenObjects", None, include_lights, include_grips)

    def invert_selected_objects(self, include_lights, include_grips):
        """        
        Inverts the current object selection.  The identifiers of the newly selected objects are returned.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly selected objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(34, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"InvertSelectedObjects", None, include_lights, include_grips)

    def last_created_objects(self, select):
        """        
        Returns the identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function.  It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the object.  If omitted, the object is not selected (False).
            
        Returns
        =======

        array
        An array of strings identifying the most recently created or changed objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(485, 1, (VT_VARIANT, 0), ((VT_BOOL, 1),), u"LastCreatedObjects", None, select)

    def last_object(self, select, include_lights, include_grips):
        """        
        Returns the identifier of the last object in the document.  The last object in the document is the first object created by the user.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the object.  If omitted, the object is not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        string
        The identifier of the object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(35, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"LastObject", None, select, include_lights, include_grips)

    def locked_objects(self, include_lights, include_grips):
        """        
        Returns the identifiers of all locked objects in the document.  Visible objects are visible and can be snapped to, but they cannot be selected.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(365, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"LockedObjects", None, include_lights, include_grips)

    def next_object(self, object, select, include_lights, include_grips):
        """        
        Returns the identifier of the next object in the document.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object from which to get the next object.
            
        select, Boolean, Optional        
        Select the object.  If omitted, the object is not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        string
        The identifier of the object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(36, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"NextObject", None, object, select, include_lights, include_grips)

    def normal_objects(self, include_lights, include_grips):
        """        
        Returns the identifiers of all normal objects in the document.  Normal objects are visible, can be snapped to, and are independent of selection state.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(364, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"NormalObjects", None, include_lights, include_grips)

    def objects_by_color(self, color, select, include_lights):
        """        
        Returns the identifiers of all objects based on the objects' color.  Object colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        color, Integer, Required        
        An RGB color value.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(37, 1, (VT_VARIANT, 0), ((VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"ObjectsByColor", None, color, select, include_lights)

    def objects_by_group(self, group, select):
        """        
        Returns the identifiers of all objects based on the objects' group name.
    
        Parameters
        ==========

        group, String, Required        
        The name of a group of objects.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(38, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"ObjectsByGroup", None, group, select)

    def objects_by_layer(self, layer, select):
        """        
        Returns the identifiers of all objects based on the objects' layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of a layer.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(39, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"ObjectsByLayer", None, layer, select)

    def objects_by_name(self, name, select, include_lights):
        """        
        Returns the identifiers of all objects based on the objects' user-assigned name.
    
        Parameters
        ==========

        name, String, Required        
        The name of an object or objects.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(40, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"ObjectsByName", None, name, select, include_lights)

    def objects_by_type(self, type, select):
        """        
        Returns the identifiers of all objects based on the objects' geometry type.
    
        Parameters
        ==========

        type, Integer, Required        
        The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(41, 1, (VT_VARIANT, 0), ((VT_I2, 1), (VT_BOOL, 1)), u"ObjectsByType", None, type, select)

    def objects_by_u_r_l(self, u_r_l, select, include_lights):
        """        
        Returns the identifiers of all objects based on the objects' user-assigned URL.
    
        Parameters
        ==========

        u_r_l, String, Required        
        The URL of an object or objects.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the objects are not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(42, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"ObjectsByURL", None, u_r_l, select, include_lights)

    def prev_selected_objects(self, select):
        """        
        Returns the identifiers of the previously selected objects.  The operation of this function is similar to that of Rhino's SelPrev command.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the object.  If omitted, the object is not selected (False).
            
        Returns
        =======

        array
        An array of strings identifying the previously selected objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(486, 1, (VT_VARIANT, 0), ((VT_BOOL, 1),), u"PrevSelectedObjects", None, select)

    def reference_objects(self, include_lights, include_grips):
        """        
        Returns the identifiers of all reference objects attached to the document.  An object from a work session reference model is a reference object.  A reference object cannot be modified.  An object is a reference object if, and only if, it is on a reference layer.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(367, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"ReferenceObjects", None, include_lights, include_grips)

    def selected_objects(self, include_lights, include_grips):
        """        
        Returns the identifiers of all objects that are currently selected.
    
        Parameters
        ==========

        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(43, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1)), u"SelectedObjects", None, include_lights, include_grips)

    def unselect_all_objects(self):
        """        
        Unselects all objects in the document.
    
        No parameters

        Returns
        =======

        number
        The number of objects that were unselected.

        """

        return self._ApplyTypes_(44, 1, (VT_VARIANT, 0), (), u"UnselectAllObjects", None, )

    def unselected_objects(self, select, include_lights, include_grips):
        """        
        Returns the identifiers of all objects that are currently unselected.
    
        Parameters
        ==========

        select, Boolean, Optional        
        Select the objects.  If omitted, the object is not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(45, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"UnselectedObjects", None, select, include_lights, include_grips)

    def visible_objects(self, view, select, include_lights, include_grips):
        """        
        Returns the identifiers of all objects that are visible in a specified view.
    
        Parameters
        ==========

        view, String, Optional        
        The title of the view.  If omitted, the current active view is used.
            
        select, Boolean, Optional        
        Select the objects.  If omitted, the object is not selected (False).
            
        include_lights, Boolean, Optional        
        Include light objects.  If omitted, light objects are not returned (False).
            
        include_grips, Boolean, Optional        
        Include grips objects.  If omitted, grips objects are not returned (False).
            
        Returns
        =======

        array
        An array of strings identifying the objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(825, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"VisibleObjects", None, view, select, include_lights, include_grips)

