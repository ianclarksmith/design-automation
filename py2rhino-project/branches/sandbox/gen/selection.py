# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Selection(IRhinoScript):



    def all_objects(self, select, include_lights, include_grips):
        """

        Returns the identifiers of all objects in the document.

        Parameters

        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(30, 1, (12, 0), ((11, 0), (11, 0), (11, 0),), u'AllObjects', None, select, include_lights, include_grips)

    def first_object(self, select, include_lights, include_grips):
        """

        Returns the identifier of the first object in the document.  The first object in the document is the last object created by the user.

        Parameters

        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        String : The identifier of the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(31, 1, (12, 0), ((11, 0), (11, 0), (11, 0),), u'FirstObject', None, select, include_lights, include_grips)

    def get_curve_object(self, message, pre_select, select):
        """

        Prompts the user to pick, or select, a single curve object.

        Parameters

        Message : Optional, String, str, String
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of selection information if successful. The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(575, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'GetCurveObject', None, message, pre_select, select)

    def get_object(self, message, type, pre_select, select, objects):
        """

        Prompts the user to pick, or select, a single object.

        Parameters

        Message : Optional, String, str, String
        Type : Optional, Number, int, Integer
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean
        Objects : Optional, Array, arrstr, Array of ?

        Returns

        String : The identifier of the picked object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(32, 1, (12, 0), ((8, 0), (2, 0), (11, 0), (11, 0), (8200, 0),), u'GetObject', None, message, type, pre_select, select, _utils.flatten(objects))

    def get_object_ex(self, message, type, pre_select, select, objects):
        """

        Prompts the user to pick, or select, a single object.

        Parameters

        Message : Optional, String, str, String
        Type : Optional, Number, int, Integer
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean
        Objects : Optional, Array, arrstr, Array of ?

        Returns

        Array : An array of selection information if successful. The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(819, 1, (12, 0), ((8, 0), (2, 0), (11, 0), (11, 0), (8200, 0),), u'GetObjectEx', None, message, type, pre_select, select, _utils.flatten(objects))

    def get_objects(self, message, type, group, pre_select, select, objects):
        """

        Prompts the user to pick or select one or more objects.

        Parameters

        Message : Optional, String, str, String
        Type : Optional, Number, int, Integer
        Group : Optional, Boolean, bln, Boolean
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean
        Objects : Optional, Array, arrstr, Array of ?

        Returns

        Array : An array of strings identifying the picked objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(33, 1, (12, 0), ((8, 0), (2, 0), (11, 0), (11, 0), (11, 0), (8200, 0),), u'GetObjects', None, message, type, group, pre_select, select, _utils.flatten(objects))

    def get_objects_ex(self, message, type, group, pre_select, select, objects):
        """

        Prompts the user to pick or select one or more objects.

        Parameters

        Message : Optional, String, str, String
        Type : Optional, Number, int, Integer
        Group : Optional, Boolean, bln, Boolean
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean
        Objects : Optional, Array, arrstr, Array of ?

        Returns

        Array : An array that contains arrays of selection information if successful. The array of selection information will contain the following:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(820, 1, (12, 0), ((8, 0), (2, 0), (11, 0), (11, 0), (11, 0), (8200, 0),), u'GetObjectsEx', None, message, type, group, pre_select, select, _utils.flatten(objects))

    def get_point_coordinates(self, message, pre_select):
        """

        Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.

        Parameters

        Message : Optional, String, str, String
        PreSelect : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of 3-D points, one for each selected point object, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(645, 1, (12, 0), ((8, 0), (11, 0),), u'GetPointCoordinates', None, message, pre_select)

    def get_surface_object(self, message, pre_select, select):
        """

        Prompts the user to pick, or select, a single surface object.

        Parameters

        Message : Optional, String, str, String
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of selection information if successful. The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(576, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'GetSurfaceObject', None, message, pre_select, select)

    def hidden_objects(self, include_lights, include_grips):
        """

        Returns the identifiers of all hidden objects in the document.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(366, 1, (12, 0), ((11, 0), (11, 0),), u'HiddenObjects', None, include_lights, include_grips)

    def invert_selected_objects(self, include_lights, include_grips):
        """

        Inverts the current object selection.  The identifiers of the newly selected objects are returned.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the newly selected objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(34, 1, (12, 0), ((11, 0), (11, 0),), u'InvertSelectedObjects', None, include_lights, include_grips)

    def last_created_objects(self, select):
        """

        Returns the identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function.  It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned.

        Parameters

        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the most recently created or changed objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(485, 1, (12, 0), ((11, 0),), u'LastCreatedObjects', None, select)

    def last_object(self, select, include_lights, include_grips):
        """

        Returns the identifier of the last object in the document.  The last object in the document is the first object created by the user.

        Parameters

        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        String : The identifier of the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(35, 1, (12, 0), ((11, 0), (11, 0), (11, 0),), u'LastObject', None, select, include_lights, include_grips)

    def locked_objects(self, include_lights, include_grips):
        """

        Returns the identifiers of all locked objects in the document.  Visible objects are visible and can be snapped to, but they cannot be selected.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(365, 1, (12, 0), ((11, 0), (11, 0),), u'LockedObjects', None, include_lights, include_grips)

    def next_object(self, object, select, include_lights, include_grips):
        """

        Returns the identifier of the next object in the document.

        Parameters

        Object : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        String : The identifier of the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(36, 1, (12, 0), ((8, 0), (11, 0), (11, 0), (11, 0),), u'NextObject', None, object, select, include_lights, include_grips)

    def normal_objects(self, include_lights, include_grips):
        """

        Returns the identifiers of all normal objects in the document.  Normal objects are visible, can be snapped to, and are independent of selection state.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(364, 1, (12, 0), ((11, 0), (11, 0),), u'NormalObjects', None, include_lights, include_grips)

    def objects_by_color(self, color, select, include_lights):
        """

        Returns the identifiers of all objects based on the objects' color.  Object colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        Color : Required, Number, lng, Integer
        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(37, 1, (12, 0), ((3, 0), (11, 0), (11, 0),), u'ObjectsByColor', None, color, select, include_lights)

    def objects_by_group(self, group, select):
        """

        Returns the identifiers of all objects based on the objects' group name.

        Parameters

        Group : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(38, 1, (12, 0), ((8, 0), (11, 0),), u'ObjectsByGroup', None, group, select)

    def objects_by_layer(self, layer, select):
        """

        Returns the identifiers of all objects based on the objects' layer.

        Parameters

        Layer : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(39, 1, (12, 0), ((8, 0), (11, 0),), u'ObjectsByLayer', None, layer, select)

    def objects_by_name(self, name, select, include_lights):
        """

        Returns the identifiers of all objects based on the objects' user-assigned name.

        Parameters

        Name : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(40, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'ObjectsByName', None, name, select, include_lights)

    def objects_by_type(self, type, select):
        """

        Returns the identifiers of all objects based on the objects' geometry type.

        Parameters

        Type : Required, Number, int, Integer
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(41, 1, (12, 0), ((2, 0), (11, 0),), u'ObjectsByType', None, type, select)

    def objects_by_u_r_l(self, u_r_l, select, include_lights):
        """

        Returns the identifiers of all objects based on the objects' user-assigned URL.

        Parameters

        URL : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(42, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'ObjectsByURL', None, u_r_l, select, include_lights)

    def prev_selected_objects(self, select):
        """

        Returns the identifiers of the previously selected objects.  The operation of this function is similar to that of Rhino's SelPrev command.

        Parameters

        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the previously selected objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(486, 1, (12, 0), ((11, 0),), u'PrevSelectedObjects', None, select)

    def reference_objects(self, include_lights, include_grips):
        """

        Returns the identifiers of all reference objects attached to the document.  An object from a work session reference model is a reference object.  A reference object cannot be modified.  An object is a reference object if, and only if, it is on a reference layer.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(367, 1, (12, 0), ((11, 0), (11, 0),), u'ReferenceObjects', None, include_lights, include_grips)

    def selected_objects(self, include_lights, include_grips):
        """

        Returns the identifiers of all objects that are currently selected.

        Parameters

        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(43, 1, (12, 0), ((11, 0), (11, 0),), u'SelectedObjects', None, include_lights, include_grips)

    def unselect_all_objects(self):
        """

        Unselects all objects in the document.

        No parameters

        Returns

        Number : The number of objects that were unselected.

        """

        return self._ApplyTypes_(44, 1, (12, 0), (,), u'UnselectAllObjects', None, )

    def unselected_objects(self, select, include_lights, include_grips):
        """

        Returns the identifiers of all objects that are currently unselected.

        Parameters

        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(45, 1, (12, 0), ((11, 0), (11, 0), (11, 0),), u'UnselectedObjects', None, select, include_lights, include_grips)

    def visible_objects(self, view, select, include_lights, include_grips):
        """

        Returns the identifiers of all objects that are visible in a specified view.

        Parameters

        View : Optional, String, str, String
        Select : Optional, Boolean, bln, Boolean
        IncludeLights : Optional, Boolean, bln, Boolean
        IncludeGrips : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(825, 1, (12, 0), ((8, 0), (11, 0), (11, 0), (11, 0),), u'VisibleObjects', None, view, select, include_lights, include_grips)

