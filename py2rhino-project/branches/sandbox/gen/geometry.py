# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Geometry(DispatchBaseClass):



    def add_clipping_plane(self, plane, d_u, d_v, view, views):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_point(self, point):
        """

        Adds a point object to the document.

        Parameters

        Point : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(68, 1, (12, 0), ((12, 0)), u'AddPoint', None, point)

    def add_point_cloud(self, points):
        """

        Adds a point cloud object to the document.

        Parameters

        Points : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(69, 1, (12, 0), ((12, 0)), u'AddPointCloud', None, points)

    def add_points(self, points):
        """

        Adds one or more point objects to the document.

        Parameters

        Points : Required, Array, arr

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(526, 1, (12, 0), ((12, 0)), u'AddPoints', None, points)

    def add_text(self, text, point, plane, height, font, style):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_text_dot(self, test, point):
        """

        Adds an annotation text dot to the document.

        Parameters

        Test : Required, String, str
        Point : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(320, 1, (12, 0), ((12, 0), (12, 0)), u'AddTextDot', None, test, point)

    def bounding_box(self, object, objects, view, world_coords):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def compare_geometry(self, object1, object2):
        """

        Compares two objects to determine if they are geometrically identical.

        Parameters

        Object1 : Required, String, str
        Object2 : Required, String, str

        Returns

        Boolean : True if the objects are geometrically identical, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(598, 1, (12, 0), ((12, 0), (12, 0)), u'CompareGeometry', None, object1, object2)

    def is_clipping_plane(self, object):
        """

        Verifies that an object is a clipping plane object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(905, 1, (12, 0), ((12, 0)), u'IsClippingPlane', None, object)

    def is_point(self, object):
        """

        Verifies an object is a point object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(120, 1, (12, 0), ((12, 0)), u'IsPoint', None, object)

    def is_point_cloud(self, object):
        """

        Verifies an object is a point cloud object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(121, 1, (12, 0), ((12, 0)), u'IsPointCloud', None, object)

    def is_text(self, object):
        """

        Verifies an object is a text object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(122, 1, (12, 0), ((12, 0)), u'IsText', None, object)

    def is_text_dot(self, object):
        """

        Verifies an object is a text dot object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(336, 1, (12, 0), ((12, 0)), u'IsTextDot', None, object)

    def point_cloud_count(self, object):
        """

        Returns the point count of a point cloud object.

        Parameters

        Object : Required, String, str

        Returns

        Number : The number of points if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(128, 1, (12, 0), ((12, 0)), u'PointCloudCount', None, object)

    def point_cloud_points(self, object):
        """

        Returns the points of a point cloud object.

        Parameters

        Object : Required, String, str

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(129, 1, (12, 0), ((12, 0)), u'PointCloudPoints', None, object)

    def point_coordinates(self, object, point):
        """

        Returns or modifies the X, Y, and Z coordinates of a point object.

        Parameters

        Object : Required, String, str
        Point : Optional, Array, arr

        Returns

        Array : If arrPoint is not specified, the current 3-D point location if successful.
        Array : If arrPoint is specified, the previous 3-D point location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(130, 1, (12, 0), ((12, 0), (12, 0)), u'PointCoordinates', None, object, point)

    def text_dot_point(self, object, point):
        """

        Returns or modifies the location, or insertion point, of an annotation text dot object.

        Parameters

        Object : Required, String, str
        Point : Optional, Array, arr

        Returns

        Array : If a new location is not specified,  the 3-D point identifying the current location if successful.
        Array : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(422, 1, (12, 0), ((12, 0), (12, 0)), u'TextDotPoint', None, object, point)

    def text_dot_text(self, object, text):
        """

        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.

        Parameters

        Object : Required, String, str
        Text : Optional, String, str

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(421, 1, (12, 0), ((12, 0), (12, 0)), u'TextDotText', None, object, text)

    def text_object_font(self, object, font):
        """

        Returns or modifies the font used by text object.

        Parameters

        Object : Required, String, str
        Font : Optional, String, str

        Returns

        String : If a font is not specified,  the current font face name if successful.
        String : If a font is specified,  the previous font face name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(474, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectFont', None, object, font)

    def text_object_height(self, object, height):
        """

        Returns or modifies the height of a text object.

        Parameters

        Object : Required, String, str
        Height : Optional, Number, dbl

        Returns

        String : If a height is not specified, the current text height if successful.
        String : If a height is specified, the previous text height if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(473, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectHeight', None, object, height)

    def text_object_plane(self, object, plane):
        """

        Returns or modifies the plane used by a text object.

        Parameters

        Object : Required, String, str
        Plane : Optional, Array, arr

        Returns

        Array : If a plane is not specified, the current plane if successful.
        Array : If a plane is specified, the previous plane if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(476, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectPlane', None, object, plane)

    def text_object_point(self, object, point):
        """

        Returns or modifies the location of a text object.

        Parameters

        Object : Required, String, str
        Point : Optional, Array, arr

        Returns

        String : If a new location is not specified,  the 3-D point identifying the current location if successful.
        String : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(471, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectPoint', None, object, point)

    def text_object_style(self, object, style):
        """

        Returns or modifies the font style of a text object.

        Parameters

        Object : Required, String, str
        Style : Optional, Number, int

        Returns

        Number : If a style is not specified,  the current font style if successful.
        Number : If a style is specified,  the previous font style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(475, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectStyle', None, object, style)

    def text_object_text(self, object, text):
        """

        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.

        Parameters

        Object : Required, String, str
        Text : Optional, String, str

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(472, 1, (12, 0), ((12, 0), (12, 0)), u'TextObjectText', None, object, text)

