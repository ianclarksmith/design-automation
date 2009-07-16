# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class ObjectGrip(IRhinoScript):



    def enable_object_grips(self, object, enable):
        """

        Enables or disables an object's grips. For curves and surfaces, these are also called control points.

        Parameters

        Object : Required, String, str, String
        Enable : Optional, Boolean, bln, Boolean

        Returns

        Boolean : True of False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(499, 1, (12, 0), ((8, 0), (11, 0),), u'EnableObjectGrips', None, object, enable)

    def get_object_grip(self, message, pre_select, select):
        """

        Prompts the user to pick or select a single object grip.

        Parameters

        Message : Optional, String, str, String
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : A one-dimensional array containing the following three elements if successful:
        String : The identifier of the object that owns the grip.
        Number : The zero-based index value of the grip.
        Array : A 3-D point identifying the location of the grip.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(561, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'GetObjectGrip', None, message, pre_select, select)

    def get_object_grips(self, message, pre_select, select):
        """

        Prompts the user to pick or select one or more object grips from one or more objects.

        Parameters

        Message : Optional, String, str, String
        PreSelect : Optional, Boolean, bln, Boolean
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : A one-dimensional array containing one or more object grip records if successful. An object grip record itself is a one-dimensional array that contains the following three elements:
        String : The identifier of the object that owns the grip.
        Number : The zero-based index value of the grip.
        Array : A 3-D point identifying the location of the grip.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(562, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'GetObjectGrips', None, message, pre_select, select)

    def next_object_grip(self, object, index, direction, enable):
        """

        Returns the next grip index from a specified grip index of an object.

        Parameters

        Object : Required, String, str, String
        Index : Required, Number, int, Integer
        Direction : Optional, Number, int, Integer
        Enable : Optional, Boolean, bln, Boolean

        Returns

        Number : The index of the next grip from the specified grip index.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(558, 1, (12, 0), ((8, 0), (2, 0), (2, 0), (11, 0),), u'NextObjectGrip', None, object, index, direction, enable)

    def object_grip_count(self, object):
        """

        Returns the number of grips owned by an object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of grips if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(500, 1, (12, 0), ((8, 0),), u'ObjectGripCount', None, object)

    def object_grip_location(self, object, index, point):
        """

        Returns or modifies the location of an object's grip.

        Parameters

        Object : Required, String, str, String
        Index : Required, Number, int, Integer
        Point : Optional, Array, arrdbl, Array of ?

        Returns

        Array : If arrPoint is not specified, the current location of the grip referenced by intIndex if successful.
        Array : If arrPoint is specified, the previous location of the grip referenced by intIndex if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(556, 1, (12, 0), ((8, 0), (2, 0), (8197, 0),), u'ObjectGripLocation', None, object, index, _utils.flatten(point))

    def object_grip_locations(self, object, points):
        """

        Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in an array of 3-D points with each position in the array corresponding to that grip's index. To modify the locations of grips, you must provide an array of 3-D points that contains the same number of points at grips.

        Parameters

        Object : Required, String, str, String
        Points : Optional, Array, arrdbl, Array of ?

        Returns

        Array : If arrPoints is not specified, the current location of all grips if successful.
        Array : If arrPoints is specified, the previous location of all grips if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(557, 1, (12, 0), ((8, 0), (8197, 0),), u'ObjectGripLocations', None, object, _utils.flatten(points))

    def object_grips_on(self, object):
        """

        Verifies that an object's grips are turned on.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True of False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(497, 1, (12, 0), ((8, 0),), u'ObjectGripsOn', None, object)

    def object_grips_selected(self, object):
        """

        Verifies that an object's grips are turned on and at least one grip is selected.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True of False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(498, 1, (12, 0), ((8, 0),), u'ObjectGripsSelected', None, object)

    def prev_object_grip(self, object, index, direction, enable):
        """

        Returns the previous grip index from a specified grip index of an object.

        Parameters

        Object : Required, String, str, String
        Index : Required, Number, int, Integer
        Direction : Optional, Number, int, Integer
        Enable : Optional, Boolean, bln, Boolean

        Returns

        Number : The index of the next grip from the specified grip index.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(559, 1, (12, 0), ((8, 0), (2, 0), (2, 0), (11, 0),), u'PrevObjectGrip', None, object, index, direction, enable)

    def select_object_grip(self, object, index):
        """

        Selects a single grip owned by an object. If the object's grips are not turned on, grips will  not be selected.

        Parameters

        Object : Required, String, str, String
        Index : Required, Number, int, Integer

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(554, 1, (12, 0), ((8, 0), (2, 0),), u'SelectObjectGrip', None, object, index)

    def select_object_grips(self, object):
        """

        Selects an object's grips. If the object's grips are not turned on, they will not be selected.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of grips selected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(501, 1, (12, 0), ((8, 0),), u'SelectObjectGrips', None, object)

    def selected_object_grips(self, object):
        """

        Returns an array of grip indices identifying an object's selected grips.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of zero-based grip indices identifying the selected grips.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(560, 1, (12, 0), ((8, 0),), u'SelectedObjectGrips', None, object)

    def unselect_object_grip(self, object, index):
        """

        Unselects a single grip owned by an object.

        Parameters

        Object : Required, String, str, String
        Index : Required, Number, int, Integer

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(555, 1, (12, 0), ((8, 0), (2, 0),), u'UnselectObjectGrip', None, object, index)

    def unselect_object_grips(self, object):
        """

        Unselects an object's grips. Note, the grips will not be turned off.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of grips unselected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(502, 1, (12, 0), ((8, 0),), u'UnselectObjectGrips', None, object)

