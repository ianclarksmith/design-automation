# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Geometry(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_clipping_plane(self, plane, d_u, d_v, views=None):
        """        
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.
    
        Parameters
        ==========

        plane, Array of ???, Required        
        The plane.
            
        d_u, Double, Required        
        The magnitude in the U direction.
            
        d_v, Double, Required        
        The magnitude in the V direction.
            
        views, Array of ???, Optional        
        The titles of the views to clip.  If omitted, the current active view is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [plane, d_u, d_v, views]
        required = [True, True, True, False]
        magic = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(plane), d_u, d_v, flatten_params(views)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(904, 1, (VT_VARIANT, 0), magic, u"AddClippingPlane", None, *flattened)

    def add_point_cloud(self, points):
        """        
        Adds a point cloud object to the document.
    
        Parameters
        ==========

        points, Array of Doubles, Required        
        An array of 3-D points.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [points]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(points)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(69, 1, (VT_VARIANT, 0), magic, u"AddPointCloud", None, *flattened)

    def add_points(self, points):
        """        
        Adds one or more point objects to the document.
    
        Parameters
        ==========

        points, Array of Doubles, Required        
        An array of 3-D points.
            
        Returns
        =======

        array
        The identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        params = [points]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(points)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(526, 1, (VT_VARIANT, 0), magic, u"AddPoints", None, *flattened)

    def add_text(self, text, point, height=None, font=None, style=None):
        """        
        Adds a text string to the document.
    
        Parameters
        ==========

        text, String, Required        
        The text to display.
            
        point, Array of ???, Required        
        A 3-D point.
            
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

        params = [text, point, height, font, style]
        required = [True, True, False, False, False]
        magic = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_I2, 1)]
        flattened = [text, flatten_params(point), height, font, style]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(76, 1, (VT_VARIANT, 0), magic, u"AddText", None, *flattened)

    def add_text_2(self, text, plane, height=None, font=None, style=None):
        """        
        Adds a text string to the document.
    
        Parameters
        ==========

        text, String, Required        
        The text to display.
            
        plane, Array of ???, Required        
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

        params = [text, plane, height, font, style]
        required = [True, True, False, False, False]
        magic = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_I2, 1)]
        flattened = [text, flatten_params(plane), height, font, style]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(76, 1, (VT_VARIANT, 0), magic, u"AddText", None, *flattened)

    def add_text_dot(self, test, point):
        """        
        Adds an annotation text dot to the document.
    
        Parameters
        ==========

        test, String, Required        
        A character or text string.
            
        point, Array of Doubles, Required        
        A 3-D point identifying the origin point.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [test, point]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [test, flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(320, 1, (VT_VARIANT, 0), magic, u"AddTextDot", None, *flattened)

    def bounding_box(self, objects, view=None, world_coords=None):
        """        
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.
    
        Parameters
        ==========

        objects, Array of ???, Required        
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

        params = [objects, view, world_coords]
        required = [True, False, False]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(objects), view, world_coords]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(117, 1, (VT_VARIANT, 0), magic, u"BoundingBox", None, *flattened)

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
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object1, object2]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(598, 1, (VT_VARIANT, 0), magic, u"CompareGeometry", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(905, 1, (VT_VARIANT, 0), magic, u"IsClippingPlane", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(120, 1, (VT_VARIANT, 0), magic, u"IsPoint", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(121, 1, (VT_VARIANT, 0), magic, u"IsPointCloud", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(122, 1, (VT_VARIANT, 0), magic, u"IsText", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(336, 1, (VT_VARIANT, 0), magic, u"IsTextDot", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(128, 1, (VT_VARIANT, 0), magic, u"PointCloudCount", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(129, 1, (VT_VARIANT, 0), magic, u"PointCloudPoints", None, *flattened)

    def point_coordinates(self, object, point=None):
        """        
        Returns or modifies the X, Y, and Z coordinates of a point object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a point object.
            
        point, Array of Doubles, Optional        
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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [object, flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(130, 1, (VT_VARIANT, 0), magic, u"PointCoordinates", None, *flattened)

    def text_dot_point(self, object, point=None):
        """        
        Returns or modifies the location, or insertion point, of an annotation text dot object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        point, Array of Doubles, Optional        
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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [object, flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(422, 1, (VT_VARIANT, 0), magic, u"TextDotPoint", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, text]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(421, 1, (VT_VARIANT, 0), magic, u"TextDotText", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, font]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(474, 1, (VT_VARIANT, 0), magic, u"TextObjectFont", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [object, height]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(473, 1, (VT_VARIANT, 0), magic, u"TextObjectHeight", None, *flattened)

    def text_object_plane(self, object, plane=None):
        """        
        Returns or modifies the plane used by a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        plane, Array of Doubles, Optional        
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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [object, flatten_params(plane)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(476, 1, (VT_VARIANT, 0), magic, u"TextObjectPlane", None, *flattened)

    def text_object_point(self, object, point=None):
        """        
        Returns or modifies the location of a text object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        point, Array of Doubles, Optional        
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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [object, flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(471, 1, (VT_VARIANT, 0), magic, u"TextObjectPoint", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [object, style]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(475, 1, (VT_VARIANT, 0), magic, u"TextObjectStyle", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, text]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(472, 1, (VT_VARIANT, 0), magic, u"TextObjectText", None, *flattened)

