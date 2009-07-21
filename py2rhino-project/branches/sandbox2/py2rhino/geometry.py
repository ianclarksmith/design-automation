# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Geometry(IRhinoScript):



    def add_clipping_plane(self, plane, d_u, d_v, view=None, views=None):
        """        
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.
            
        d_u, Double, Required        
        The magnitude in the U direction.
            
        d_v, Double, Required        
        The magnitude in the V direction.
            
        view, String, Optional        
        The title of the view to clip.  If omitted, the current active view is used.
            
        views, Array of ????, Optional        
        The titles of the views to clip.  If omitted, the current active view is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [plane, d_u, d_v, view, views]
        params_required = [True, True, True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), d_u, d_v, view, flatten(views)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(904, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddClippingPlane", None, *params_flattened)

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

        params = [point]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(68, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPoint", None, *params_flattened)

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

        params = [points]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(69, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPointCloud", None, *params_flattened)

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

        params = [points]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(526, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPoints", None, *params_flattened)

    def add_text(self, text, point, plane, height=None, font=None, style=None):
        """        
        Adds a text string to the document.
    
        Parameters
        ==========

        text, String, Required        
        The text to display.
            
        point, Array of ????, Required        
        A 3-D point.
            
        plane, Array of ????, Required        
        The plane on which the text will lie.  The origin of the plane will be the origin point of the text.
            
        height, Double, Optional        
        The text height.  If omitted, a height of 1.0 units is used.
            
        font, String, Optional        
        The text font.  If omitted, the Arial font is used.
            
        style, Integer, Optional        
        The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [text, point, plane, height, font, style]
        params_required = [True, True, True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [text, flatten(point), flatten(plane), height, font, style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(76, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddText", None, *params_flattened)

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

        params = [test, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [test, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(320, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddTextDot", None, *params_flattened)

    def bounding_box(self, object, objects, view=None, world_coords=None):
        """        
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        objects, Array of ????, Required        
        An array of strings identifying the objects.
            
        view, String, Optional        
        The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
            
        world_coords, Boolean, Optional        
        Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.
            
        Returns
        =======

        array
        An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.

        null
        If not successful, or on error.

        """

        params = [object, objects, view, world_coords]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, flatten(objects), view, world_coords]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(117, 1, (VT_VARIANT, 0), params_magic_numbers, u"BoundingBox", None, *params_flattened)

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

        params = [object1, object2]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object1, object2]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(598, 1, (VT_VARIANT, 0), params_magic_numbers, u"CompareGeometry", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(905, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsClippingPlane", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(120, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPoint", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(121, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPointCloud", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(122, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsText", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(336, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsTextDot", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(128, 1, (VT_VARIANT, 0), params_magic_numbers, u"PointCloudCount", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(129, 1, (VT_VARIANT, 0), params_magic_numbers, u"PointCloudPoints", None, *params_flattened)

    def point_coordinates(self, object, point=None):
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

        params = [object, point]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(130, 1, (VT_VARIANT, 0), params_magic_numbers, u"PointCoordinates", None, *params_flattened)

    def text_dot_point(self, object, point=None):
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

        params = [object, point]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(422, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextDotPoint", None, *params_flattened)

    def text_dot_text(self, object, text=None):
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

        params = [object, text]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(421, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextDotText", None, *params_flattened)

    def text_object_font(self, object, font=None):
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

        params = [object, font]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, font]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(474, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectFont", None, *params_flattened)

    def text_object_height(self, object, height=None):
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

        params = [object, height]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, height]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(473, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectHeight", None, *params_flattened)

    def text_object_plane(self, object, plane=None):
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

        params = [object, plane]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(476, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectPlane", None, *params_flattened)

    def text_object_point(self, object, point=None):
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

        params = [object, point]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(471, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectPoint", None, *params_flattened)

    def text_object_style(self, object, style=None):
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

        params = [object, style]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(475, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectStyle", None, *params_flattened)

    def text_object_text(self, object, text=None):
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

        params = [object, text]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(472, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextObjectText", None, *params_flattened)

