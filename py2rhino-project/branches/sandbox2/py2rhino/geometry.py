# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Geometry(IRhinoScript):



    def add_clipping_plane(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_point(self, point):
        """        
        Adds a point object to the document.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(68, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"AddPoint", None, flatten(point))

    def add_point_cloud(self, points):
        """        
        Adds a point cloud object to the document.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(69, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"AddPointCloud", None, flatten(points))

    def add_points(self, points):
        """        
        Adds one or more point objects to the document.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        Returns
        =======

        array
        The identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(526, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"AddPoints", None, flatten(points))

    def add_text(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_text_dot(self, test, point):
        """        
        Adds an annotation text dot to the document.
    
        Parameters
        ==========

        test, String, Required        
        A character or text string.
            
        point, Array of ????, Required        
        A 3-D point identifying the origin point.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(320, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"AddTextDot", None, test, flatten(point))

    def bounding_box(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def compare_geometry(self, object1, object2):
        """        
        Compares two objects to determine if they are geometrically identical.
    
        Parameters
        ==========

        object1, String, Required        
        The identifier of the first object to compare.
            
        object2, String, Required        
        The identifier of the second object to compare.
            
        Returns
        =======

        boolean
        True if the objects are geometrically identical, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(598, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"CompareGeometry", None, object1, object2)

    def is_clipping_plane(self, object):
        """        
        Verifies that an object is a clipping plane object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(905, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsClippingPlane", None, object)

    def is_point(self, object):
        """        
        Verifies an object is a point object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(120, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsPoint", None, object)

    def is_point_cloud(self, object):
        """        
        Verifies an object is a point cloud object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(121, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsPointCloud", None, object)

    def is_text(self, object):
        """        
        Verifies an object is a text object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(122, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsText", None, object)

    def is_text_dot(self, object):
        """        
        Verifies an object is a text dot object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(336, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsTextDot", None, object)

    def point_cloud_count(self, object):
        """        
        Returns the point count of a point cloud object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a point cloud object.
            
        Returns
        =======

        number
        The number of points if successful

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(128, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"PointCloudCount", None, object)

    def point_cloud_points(self, object):
        """        
        Returns the points of a point cloud object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a point cloud object.
            
        Returns
        =======

        array
        An array of 3-D points if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(129, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"PointCloudPoints", None, object)

    def point_coordinates(self, object, point):
        """        
        Returns or modifies the X, Y, and Z coordinates of a point object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a point object.
            
        point, Array of ????, Optional        
        A new 3-D point location.
            
        Returns
        =======

        array
        If arrPoint is not specified, the current 3-D point location if successful.

        array
        If arrPoint is specified, the previous 3-D point location if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(130, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"PointCoordinates", None, object, flatten(point))

    def text_dot_point(self, object, point):
        """        
        Returns or modifies the location, or insertion point, of an annotation text dot object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        point, Array of ????, Optional        
        A 3-D point identifying the new location point.
            
        Returns
        =======

        array
        If a new location is not specified,  the 3-D point identifying the current location if successful.

        array
        If a new location is specified,  the 3-D point identifying the previous location if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(422, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"TextDotPoint", None, object, flatten(point))

    def text_dot_text(self, object, text):
        """        
        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        text, String, Optional        
        A new character or text string.
            
        Returns
        =======

        string
        If a new text string is not specified,  the current string value if successful.

        string
        If a new text string is specified,  the previous string value if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(421, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"TextDotText", None, object, text)

    def text_object_font(self, object, font):
        """        
        Returns or modifies the font used by text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        font, String, Optional        
        The new font face name.  If omitted, the current font is returned.
            
        Returns
        =======

        string
        If a font is not specified,  the current font face name if successful.

        string
        If a font is specified,  the previous font face name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(474, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"TextObjectFont", None, object, font)

    def text_object_height(self, object, height):
        """        
        Returns or modifies the height of a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        height, Double, Optional        
        The new text height.  If omitted, the current text height is returned.
            
        Returns
        =======

        string
        If a height is not specified, the current text height if successful.

        string
        If a height is specified, the previous text height if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(473, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"TextObjectHeight", None, object, height)

    def text_object_plane(self, object, plane):
        """        
        Returns or modifies the plane used by a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        plane, Array of ????, Optional        
        The new construction plane.  The elements of a plane array are as follows:
		Value
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        If a plane is not specified, the current plane if successful.

        array
        If a plane is specified, the previous plane if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(476, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"TextObjectPlane", None, object, flatten(plane))

    def text_object_point(self, object, point):
        """        
        Returns or modifies the location of a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        point, Array of ????, Optional        
        A 3-D point identifying the new location point.
            
        Returns
        =======

        string
        If a new location is not specified,  the 3-D point identifying the current location if successful.

        string
        If a new location is specified,  the 3-D point identifying the previous location if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(471, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"TextObjectPoint", None, object, flatten(point))

    def text_object_style(self, object, style):
        """        
        Returns or modifies the font style of a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        style, Integer, Optional        
        The font style.  If omitted, the current font style is returned.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal.
		1
		Bold.
		2
            
        Returns
        =======

        number
        If a style is not specified,  the current font style if successful.

        number
        If a style is specified,  the previous font style if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(475, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"TextObjectStyle", None, object, style)

    def text_object_text(self, object, text):
        """        
        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        text, String, Optional        
        A new character or text string.
            
        Returns
        =======

        string
        If a new text string is not specified,  the current string value if successful.

        string
        If a new text string is specified,  the previous string value if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(472, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"TextObjectText", None, object, text)

