

class clipping_pane():

        add_clipping_plane = """
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.
        d_u  (float, Required) - The magnitude in the U direction.
        d_v  (float, Required) - The magnitude in the V direction.
        views  (List of string, Optional) - The titles of the views to clip.  If omitted, the current active view is used.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddClippingPlane

        """


class geom():

        bounding_box = """
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.

        Parameters
        ==========
        objects  (List of string, Required) - An list of strings identifying the objects.
        view  (string, Optional) - The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
        world_coords  (boolean, Optional) - Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.

        Returns
        =======
        list - A list of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BoundingBox

        """
        compare_geometry = """
        Compares two objects to determine if they are geometrically identical.

        Parameters
        ==========
        object_1  (string, Required) - The identifier of the first object to compare.
        object_2  (string, Required) - The identifier of the second object to compare.

        Returns
        =======
        boolean - True if the objects are geometrically identical, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CompareGeometry

        """


class point():

        add_point = """
        Adds a point object to the document.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPoint

        """
        add_points = """
        Adds one or more point objects to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.

        Returns
        =======
        list - The identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPoints

        """


class point_cloud():

        add_point_cloud = """
        Adds a point cloud object to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPointCloud

        """
        point_cloud_count = """
        Returns the point count of a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The identifier of a point cloud object.

        Returns
        =======
        number - The number of points if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointCloudCount

        """
        point_cloud_points = """
        Returns the points of a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The identifier of a point cloud object.

        Returns
        =======
        list - A list of 3-D points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointCloudPoints

        """


class text():

        add_text = """
        Adds a text string to the document.

        Parameters
        ==========
        text  (string, Required) - The text to display.
        point  (List of float, Required) - A 3-D point.
        height  (float, Optional) - The text height.  If omitted, a height of 1.0 units is used.
        font  (string, Optional) - The text font.  If omitted, the Arial font is used.
        style  (integer, Optional) - The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddText

        """
        add_text_2 = """
        Adds a text string to the document.

        Parameters
        ==========
        text  (string, Required) - The text to display.
        plane  (List of float, Required) - The plane on which the text will lie.  The origin of the plane will be the origin point of the text.
        height  (float, Optional) - The text height.  If omitted, a height of 1.0 units is used.
        font  (string, Optional) - The text font.  If omitted, the Arial font is used.
        style  (integer, Optional) - The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddText

        """
        add_text_dot = """
        Adds an annotation text dot to the document.

        Parameters
        ==========
        test  (string, Required) - A character or text string.
        point  (List of float, Required) - A 3-D point identifying the origin point.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddTextDot

        """
        text_dot_point = """
        Returns or modifies the location, or insertion point, of an annotation text dot object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        point  (List of float, Optional) - A 3-D point identifying the new location point.

        Returns
        =======
        list - If a new location is not specified,  the 3-D point identifying the current location if successful.
        list - If a new location is specified,  the 3-D point identifying the previous location if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextDotPoint

        """
        text_dot_text = """
        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        text  (string, Optional) - A new character or text string.

        Returns
        =======
        string - If a new text string is not specified,  the current string value if successful.
        string - If a new text string is specified,  the previous string value if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextDotText

        """
        text_object_font = """
        Returns or modifies the font used by text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        font  (string, Optional) - The new font face name.  If omitted, the current font is returned.

        Returns
        =======
        string - If a font is not specified,  the current font face name if successful.
        string - If a font is specified,  the previous font face name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectFont

        """
        text_object_height = """
        Returns or modifies the height of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        height  (float, Optional) - The new text height.  If omitted, the current text height is returned.

        Returns
        =======
        string - If a height is not specified, the current text height if successful.
        string - If a height is specified, the previous text height if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectHeight

        """
        text_object_plane = """
        Returns or modifies the plane used by a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        plane  (List of float, Optional) - The new construction plane.  The elements of a plane list are as follows:
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
        list - If a plane is not specified, the current plane if successful.
        list - If a plane is specified, the previous plane if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectPlane

        """
        text_object_point = """
        Returns or modifies the location of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        point  (List of float, Optional) - A 3-D point identifying the new location point.

        Returns
        =======
        string - If a new location is not specified,  the 3-D point identifying the current location if successful.
        string - If a new location is specified,  the 3-D point identifying the previous location if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectPoint

        """
        text_object_style = """
        Returns or modifies the font style of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        style  (integer, Optional) - The font style.  If omitted, the current font style is returned.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal.
		1
		Bold.
		2

        Returns
        =======
        number - If a style is not specified,  the current font style if successful.
        number - If a style is specified,  the previous font style if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectStyle

        """
        text_object_text = """
        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        text  (string, Optional) - A new character or text string.

        Returns
        =======
        string - If a new text string is not specified,  the current string value if successful.
        string - If a new text string is specified,  the previous string value if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectText

        """
