# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Geometry(DispatchBaseClass):



    def addclippingplane(self, arrplane, dbldu, dbldv, strview, arrviews):
        """

        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.

        Parameters

        arrPlane : Required,   Array,   The plane
        dblDU : Required,   Number,   The magnitude in the U direction
        dblDV : Required,   Number,   The magnitude in the V direction
        strView : Optional,   String,   The title of the view to clip
        arrViews : Optional,   Array,   The titles of the views to clip

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddClippingPlane', None, arrPlane, dblDU, dblDV, strView, arrViews)

    def addpoint(self, arrpoint):
        """

        Adds a point object to the document.

        Parameters

        arrPoint : Required,   Array,   A 3-D point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPoint', None, arrPoint)

    def addpointcloud(self, arrpoints):
        """

        Adds a point cloud object to the document.

        Parameters

        arrPoints : Required,   Array,   An array of 3-D points

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPointCloud', None, arrPoints)

    def addpoints(self, arrpoints):
        """

        Adds one or more point objects to the document.

        Parameters

        arrPoints : Required,   Array,   An array of 3-D points

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPoints', None, arrPoints)

    def addtext(self, strtext, arrpoint, arrplane, dblheight, strfont, intstyle):
        """

        Adds a text string to the document.

        Parameters

        strText : Required,  String,   The text to display
        arrPoint : Required,   Array,   A 3-D point
        arrPlane : Required,   Array,   The plane on which the text will lie
        dblHeight : Optional,   Number,   The text height
        strFont : Optional,   String,   The text font
        intStyle : Optional,  Number,   The font style

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddText', None, strText, arrPoint, arrPlane, dblHeight, strFont, intStyle)

    def addtextdot(self, strtest, arrpoint):
        """

        Adds an annotation text dot to the document.

        Parameters

        strTest : Required,   String,   A character or text string
        arrPoint : Required,   Array,   A 3-D point identifying the origin point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddTextDot', None, strTest, arrPoint)

    def boundingbox(self, strobject, arrobjects, strview, blnworldcoords):
        """

        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.

        Parameters

        strObject : Required,   String,   The identifier of the object
        arrObjects : Required,   Array,   An array of strings identifying the objects
        strView : Optional,   String,   The title of the view that contains the construction plane to which the bounding box should be aligned
        blnWorldCoords : Optional,   Boolean,   Whether or not to return the bounding box as world coordinates or construction plane coordinates

        Returns

        Array : An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BoundingBox', None, strObject, arrObjects, strView, blnWorldCoords)

    def comparegeometry(self, strobject1, strobject2):
        """

        Compares two objects to determine if they are geometrically identical.

        Parameters

        strObject1 : Required,   String,   The identifier of the first object to compare
        strObject2 : Required,   String,   The identifier of the second object to compare

        Returns

        Boolean : True if the objects are geometrically identical, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CompareGeometry', None, strObject1, strObject2)

    def isclippingplane(self, strobject):
        """

        Verifies that an object is a clipping plane object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsClippingPlane', None, strObject)

    def ispoint(self, strobject):
        """

        Verifies an object is a point object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPoint', None, strObject)

    def ispointcloud(self, strobject):
        """

        Verifies an object is a point cloud object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointCloud', None, strObject)

    def istext(self, strobject):
        """

        Verifies an object is a text object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsText', None, strObject)

    def istextdot(self, strobject):
        """

        Verifies an object is a text dot object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsTextDot', None, strObject)

    def pointcloudcount(self, strobject):
        """

        Returns the point count of a point cloud object.

        Parameters

        strObject : Required,   String,   The identifier of a point cloud object

        Returns

        Number : The number of points if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCloudCount', None, strObject)

    def pointcloudpoints(self, strobject):
        """

        Returns the points of a point cloud object.

        Parameters

        strObject : Required,   String,   The identifier of a point cloud object

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCloudPoints', None, strObject)

    def pointcoordinates(self, strobject, arrpoint):
        """

        Returns or modifies the X, Y, and Z coordinates of a point object.

        Parameters

        strObject : Required,   String,   The identifier of a point object
        arrPoint : Optional,   Array,   A new 3-D point location

        Returns

        Array : If arrPoint is not specified, the current 3-D point location if successful.
        Array : If arrPoint is specified, the previous 3-D point location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCoordinates', None, strObject, arrPoint)

    def textdotpoint(self, strobject, arrpoint):
        """

        Returns or modifies the location, or insertion point, of an annotation text dot object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        arrPoint : Optional,   Array,   A 3-D point identifying the new location point

        Returns

        Array : If a new location is not specified,  the 3-D point identifying the current location if successful.
        Array : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextDotPoint', None, strObject, arrPoint)

    def textdottext(self, strobject, strtext):
        """

        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.

        Parameters

        strObject : Required,   String,   The identifier of the object
        strText : Optional,   String,   A new character or text string

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextDotText', None, strObject, strText)

    def textobjectfont(self, strobject, strfont):
        """

        Returns or modifies the font used by text object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        strFont : Optional,   String,   The new font face name

        Returns

        String : If a font is not specified,  the current font face name if successful.
        String : If a font is specified,  the previous font face name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectFont', None, strObject, strFont)

    def textobjectheight(self, strobject, dblheight):
        """

        Returns or modifies the height of a text object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        dblHeight : Optional,   Number,   The new text height

        Returns

        String : If a height is not specified, the current text height if successful.
        String : If a height is specified, the previous text height if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectHeight', None, strObject, dblHeight)

    def textobjectplane(self, strobject, arrplane, 0, 1, 2, 3):
        """

        Returns or modifies the plane used by a text object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        arrPlane : Optional,   Array,  The new construction plane
        0 : Required,   The construction plane's origin (3-D point), 
        1 : Required,   The construction plane's X axis direction (3-D vector), 
        2 : Required,   The construction plane's Y axis direction (3-D vector), 
        3 : Optional,   The construction plane's Z axis direction (3-D vector), 

        Returns

        Array : If a plane is not specified, the current plane if successful.
        Array : If a plane is specified, the previous plane if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectPlane', None, strObject, arrPlane, 0, 1, 2, 3)

    def textobjectpoint(self, strobject, arrpoint):
        """

        Returns or modifies the location of a text object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        arrPoint : Optional,   Array,   A 3-D point identifying the new location point

        Returns

        String : If a new location is not specified,  the 3-D point identifying the current location if successful.
        String : If a new location is specified,  the 3-D point identifying the previous location if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectPoint', None, strObject, arrPoint)

    def textobjectstyle(self, strobject, intstyle):
        """

        Returns or modifies the font style of a text object.

        Parameters

        strObject : Required,   String,   The identifier of the object
        intStyle : Optional,  Number,   The font style

        Returns

        Number : If a style is not specified,  the current font style if successful.
        Number : If a style is specified,  the previous font style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectStyle', None, strObject, intStyle)

    def textobjecttext(self, strobject, strtext):
        """

        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.

        Parameters

        strObject : Required,   String,   The identifier of the object
        strText : Optional,   String,   A new character or text string

        Returns

        String : If a new text string is not specified,  the current string value if successful.
        String : If a new text string is specified,  the previous string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextObjectText', None, strObject, strText)

