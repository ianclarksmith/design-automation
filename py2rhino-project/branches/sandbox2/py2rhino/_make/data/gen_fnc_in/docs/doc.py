

class object_type():

        is_clipping_plane = """
        Verifies that an object is a clipping plane object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsClippingPlane

        """
        is_point = """
        Verifies an object is a point object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPoint

        """
        is_point_cloud = """
        Verifies an object is a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPointCloud

        """
        is_text = """
        Verifies an object is a text object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsText

        """
        is_text_dot = """
        Verifies an object is a text dot object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsTextDot

        """


class select():

        all_objects = """
        Returns the identifiers of all objects in the document.

        Parameters
        ==========
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AllObjects

        """
        first_object = """
        Returns the identifier of the first object in the document.  The first object in the document is the last object created by the user.

        Parameters
        ==========
        select  (boolean, Optional) - Select the object.  If omitted, the object is not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        string - The object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FirstObject

        """
        get_crv_object = """
        Prompts the user to pick, or select, a single curve object.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Select the picked objects.  If omitted, the objects that are picked are not selected (False).

        Returns
        =======
        list - A list of selection information if successful. The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetCurveObject

        """
        get_object = """
        Prompts the user to pick, or select, a single object.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        type  (integer, Optional) - The type or types of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
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
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
        objects  (List of string, Optional) - An list of strings identifying the objects that are allowed to be selected.

        Returns
        =======
        string - The picked object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetObject

        """
        get_object_ex = """
        Prompts the user to pick, or select, a single object.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        type  (integer, Optional) - The type or types of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
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
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
        objects  (List of string, Optional) - An list of strings identifying the objects that are allowed to be selected.

        Returns
        =======
        list - A list of selection information if successful. The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetObjectEx

        """
        get_objects = """
        Prompts the user to pick or select one or more objects.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        type  (integer, Optional) - The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
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
        group  (boolean, Optional) - Honor object grouping.  If omitted and the user picks a group, the entire group will be picked (True). Note, if intType is set to a value other than 0 (All objects), then group selection will be disabled.
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
        objects  (List of string, Optional) - An list of strings identifying the objects that are allowed to be selected.

        Returns
        =======
        list - A list of strings identifying the picked objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetObjects

        """
        get_objects_ex = """
        Prompts the user to pick or select one or more objects.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        type  (integer, Optional) - The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
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
        group  (boolean, Optional) - Honor object grouping.  If omitted and the user picks a group, the entire group will be picked (True). Note, if intType is set to a value other than 0 (All objects), then group selection will be disabled.
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Specifies whether or not the picked objects will remain selected when the function ends.  If omitted, objects that were pre-picked will remain selected and the objects that were post-picked will not be selected.
        objects  (List of string, Optional) - An list of strings identifying the objects that are allowed to be selected.

        Returns
        =======
        list - A list that contains lists of selection information if successful. The list of selection information will contain the following:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetObjectsEx

        """
        get_point_coords = """
        Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).

        Returns
        =======
        list - A list of 3-D points, one for each selected point object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetPointCoordinates

        """
        get_srf_object = """
        Prompts the user to pick, or select, a single surface object.

        Parameters
        ==========
        message  (string, Optional) - A prompt or message.
        pre_select  (boolean, Optional) - Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
        select  (boolean, Optional) - Select the picked objects.  If omitted, the objects that are picked are not selected (False).

        Returns
        =======
        list - A list of selection information if successful. The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetSurfaceObject

        """
        hidden_objects = """
        Returns the identifiers of all hidden objects in the document.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: HiddenObjects

        """
        invert_selected_objects = """
        Inverts the current object selection.  The identifiers of the newly selected objects are returned.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the newly selected objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InvertSelectedObjects

        """
        last_created_objects = """
        Returns the identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function.  It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned.

        Parameters
        ==========
        select  (boolean, Optional) - Select the object.  If omitted, the object is not selected (False).

        Returns
        =======
        list - A list of strings identifying the most recently created or changed objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LastCreatedObjects

        """
        last_object = """
        Returns the identifier of the last object in the document.  The last object in the document is the first object created by the user.

        Parameters
        ==========
        select  (boolean, Optional) - Select the object.  If omitted, the object is not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        string - The object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LastObject

        """
        locked_objects = """
        Returns the identifiers of all locked objects in the document.  Visible objects are visible and can be snapped to, but they cannot be selected.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LockedObjects

        """
        next_object = """
        Returns the identifier of the next object in the document.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object from which to get the next object.
        select  (boolean, Optional) - Select the object.  If omitted, the object is not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        string - The object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: NextObject

        """
        normal_objects = """
        Returns the identifiers of all normal objects in the document.  Normal objects are visible, can be snapped to, and are independent of selection state.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: NormalObjects

        """
        objects_by_color = """
        Returns the identifiers of all objects based on the objects' color.  Object colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Required) - An RGB color value.
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByColor

        """
        objects_by_group = """
        Returns the identifiers of all objects based on the objects' group name.

        Parameters
        ==========
        group  (string, Required) - The name of a group of objects.
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByGroup

        """
        objects_by_layer = """
        Returns the identifiers of all objects based on the objects' layer.

        Parameters
        ==========
        layer  (string, Required) - The name of a layer.
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByLayer

        """
        objects_by_name = """
        Returns the identifiers of all objects based on the objects' user-assigned name.

        Parameters
        ==========
        name  (string, Required) - The name of an object or objects.
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByName

        """
        objects_by_type = """
        Returns the identifiers of all objects based on the objects' geometry type.

        Parameters
        ==========
        type  (integer, Required) - The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
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
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByType

        """
        objects_by_url = """
        Returns the identifiers of all objects based on the objects' user-assigned URL.

        Parameters
        ==========
        url  (string, Required) - The URL of an object or objects.
        select  (boolean, Optional) - Select the objects.  If omitted, the objects are not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectsByURL

        """
        prev_selected_objects = """
        Returns the identifiers of the previously selected objects.  The operation of this function is similar to that of Rhino's SelPrev command.

        Parameters
        ==========
        select  (boolean, Optional) - Select the object.  If omitted, the object is not selected (False).

        Returns
        =======
        list - A list of strings identifying the previously selected objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PrevSelectedObjects

        """
        reference_objects = """
        Returns the identifiers of all reference objects attached to the document.  An object from a work session reference model is a reference object.  A reference object cannot be modified.  An object is a reference object if, and only if, it is on a reference layer.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ReferenceObjects

        """
        selected_objects = """
        Returns the identifiers of all objects that are currently selected.

        Parameters
        ==========
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SelectedObjects

        """
        unselect_all_objects = """
        Unselects all objects in the document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects that were unselected.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnselectAllObjects

        """
        unselected_objects = """
        Returns the identifiers of all objects that are currently unselected.

        Parameters
        ==========
        select  (boolean, Optional) - Select the objects.  If omitted, the object is not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnselectedObjects

        """
        visible_objects = """
        Returns the identifiers of all objects that are visible in a specified view.

        Parameters
        ==========
        view  (string, Optional) - The title of the view.  If omitted, the current active view is used.
        select  (boolean, Optional) - Select the objects.  If omitted, the object is not selected (False).
        include_lights  (boolean, Optional) - Include light objects.  If omitted, light objects are not returned (False).
        include_grips  (boolean, Optional) - Include grips objects.  If omitted, grips objects are not returned (False).

        Returns
        =======
        list - A list of strings identifying the objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VisibleObjects

        """
