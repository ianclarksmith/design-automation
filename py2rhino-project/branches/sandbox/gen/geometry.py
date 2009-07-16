# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Geometry(DispatchBaseClass):



        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_point(self, arr_point):
        """

        Adds a point object to the document.

        Parameters

        arrPoint : Required, Array, A 3-D point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPoint', None, arrPoint)

    def add_point_cloud(self, arr_points):
        """

        Adds a point cloud object to the document.

        Parameters

        arrPoints : Required, Array, An array of 3-D points

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPointCloud', None, arrPoints)

    def add_points(self, arr_points):
        """

        Adds one or more point objects to the document.

        Parameters

        arrPoints : Required, Array, An array of 3-D points

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPoints', None, arrPoints)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_text_dot(self, str_test, arr_point):
        """

        Adds an annotation text dot to the document.

        Parameters

        strTest : Required, String, A character or text string
        arrPoint : Required, Array, A 3-D point identifying the origin point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddTextDot', None, strTest, arrPoint)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def compare_geometry(self, str_object1, str_object2):
        """

        Compares two objects to determine if they are geometrically identical.

        Parameters

        strObject1 : Required, String, The identifier of the first object to compare
        strObject2 : Required, String, The identifier of the second object to compare

        Returns

        Boolean : True if the objects are geometrically identical, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CompareGeometry', None, strObject1, strObject2)

    def is_clipping_plane(self, str_object):
        """

        Verifies that an object is a clipping plane object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsClippingPlane', None, strObject)

    def is_point(self, str_object):
        """

        Verifies an object is a point object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPoint', None, strObject)

    def is_point_cloud(self, str_object):
        """

        Verifies an object is a point cloud object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointCloud', None, strObject)

    def is_text(self, str_object):
        """

        Verifies an object is a text object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsText', None, strObject)

    def is_text_dot(self, str_object):
        """

        Verifies an object is a text dot object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsTextDot', None, strObject)

    def point_cloud_count(self, str_object):
        """

        Returns the point count of a point cloud object.

        Parameters

        strObject : Required, String, The identifier of a point cloud object

        Returns

        Number : The number of points if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCloudCount', None, strObject)

    def point_cloud_points(self, str_object):
        """

        Returns the points of a point cloud object.

        Parameters

        strObject : Required, String, The identifier of a point cloud object

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCloudPoints', None, strObject)

    def point_coordinates(self, str_object, arr_point):
        """

        Returns or modifies the X, Y, and Z coordinates of a point object.

        Parameters

        strObject : Required, String, The identifier of a point object
        arrPoint : Optional, Array, A new 3-D point location

        Returns

        Array : If arrPoint is not specified, the current 3-D point location if successful.
        Array : If arrPoint is specified, the previous 3-D point location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCoordinates', None, strObject, arrPoint)

    def text_dot_point(self, str_object, arr_point):
        """

        Returns or modifies the location, or insertion point, of an annotation text dot object.

        Parameters

        strObject : Required, String, The identifier of the object
        arrPoint : Optional, Array, A 3-D point identifying the new location point

        Returns

        Array : If a new location is not specified,  the 3-D point identifying the current location if successful.
        Array : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextDotPoint', None, strObject, arrPoint)

    def text_dot_text(self, str_object, str_text):
        """

        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.

        Parameters

        strObject : Required, String, The identifier of the object
        strText : Optional, String, A new character or text string

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextDotText', None, strObject, strText)

    def text_object_font(self, str_object, str_font):
        """

        Returns or modifies the font used by text object.

        Parameters

        strObject : Required, String, The identifier of the object
        strFont : Optional, String, The new font face name

        Returns

        String : If a font is not specified,  the current font face name if successful.
        String : If a font is specified,  the previous font face name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectFont', None, strObject, strFont)

    def text_object_height(self, str_object, dbl_height):
        """

        Returns or modifies the height of a text object.

        Parameters

        strObject : Required, String, The identifier of the object
        dblHeight : Optional, Number, The new text height

        Returns

        String : If a height is not specified, the current text height if successful.
        String : If a height is specified, the previous text height if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectHeight', None, strObject, dblHeight)

    def text_object_plane(self, str_object, arr_plane):
        """

        Returns or modifies the plane used by a text object.

        Parameters

        strObject : Required, String, The identifier of the object
        arrPlane : Optional, Array, The new construction plane

        Returns

        Array : If a plane is not specified, the current plane if successful.
        Array : If a plane is specified, the previous plane if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectPlane', None, strObject, arrPlane)

    def text_object_point(self, str_object, arr_point):
        """

        Returns or modifies the location of a text object.

        Parameters

        strObject : Required, String, The identifier of the object
        arrPoint : Optional, Array, A 3-D point identifying the new location point

        Returns

        String : If a new location is not specified,  the 3-D point identifying the current location if successful.
        String : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectPoint', None, strObject, arrPoint)

    def text_object_style(self, str_object, int_style):
        """

        Returns or modifies the font style of a text object.

        Parameters

        strObject : Required, String, The identifier of the object
        intStyle : Optional, Number, The font style

        Returns

        Number : If a style is not specified,  the current font style if successful.
        Number : If a style is specified,  the previous font style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectStyle', None, strObject, intStyle)

    def text_object_text(self, str_object, str_text):
        """

        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.

        Parameters

        strObject : Required, String, The identifier of the object
        strText : Optional, String, A new character or text string

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectText', None, strObject, strText)

