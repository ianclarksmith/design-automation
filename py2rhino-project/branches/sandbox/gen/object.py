# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Object(DispatchBaseClass):



    def add_object_mesh(self, str_object, int_quality, bln_enable):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of a meshable object
        intQuality : Optional, Number, The initial settings of the new custom render mesh parameters
        blnEnable : Optional, Boolean, Enable the custom render mesh parameters

        Returns

        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddObjectMesh', None, strObject, intQuality, blnEnable)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def delete_object(self, str_object):
        """

        Deletes a single object from the document.

        Parameters

        strObject : Required, String, The identifier of the object to delete

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteObject', None, strObject)

    def delete_objects(self, arr_objects):
        """

        Deletes one or more objects from the document.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to delete

        Returns

        Number : The number of objects deleted if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteObjects', None, arrObjects)

    def enable_object_mesh(self, arr_objects, bln_enable):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        arrObjects : Required, Object, The identifier of a meshable object
        blnEnable : Optional, Boolean, Enable the custom render mesh settings

        Returns

        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EnableObjectMesh', None, arrObjects, blnEnable)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def hide_object(self, str_object):
        """

        Hides a single object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strObject : Required, String, The identifier of the object to hide

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'HideObject', None, strObject)

    def hide_objects(self, arr_objects):
        """

        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to hide

        Returns

        Number : The number of objects hidden if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'HideObjects', None, arrObjects)

    def is_layout_object(self, str_object):
        """

        Verifies that an object is in either page layout space or model space.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsLayoutObject', None, strObject)

    def is_object(self, str_object):
        """

        Verifies the existence of an object.

        Parameters

        strObject : Required, String, The identifier of an object

        No returns


        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObject', None, strObject)

    def is_object_hidden(self, str_object):
        """

        Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectHidden', None, strObject)

    def is_object_in_box(self, str_object, arr_box, bln_mode):
        """

        Verifies an object's bounding box is inside of another bounding box.

        Parameters

        strObject : Required, String, The identifier of an object
        arrBox : Required, Array, The bounding box to test against
        blnMode : Optional, Boolean, The test mode

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectInBox', None, strObject, arrBox, blnMode)

    def is_object_in_group(self, str_object, str_group):
        """

        Verifies that an object is a member of a specified group.

        Parameters

        strObject : Required, String, The identifier of an object
        strGroup : Optional, String, The name of a group

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectInGroup', None, strObject, strGroup)

    def is_object_locked(self, str_object):
        """

        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectLocked', None, strObject)

    def is_object_normal(self, str_object):
        """

        Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectNormal', None, strObject)

    def is_object_reference(self, str_object):
        """

        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectReference', None, strObject)

    def is_object_selectable(self, str_object):
        """

        Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectSelectable', None, strObject)

    def is_object_selected(self, str_object):
        """

        Verifies that an object is currently selected.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectSelected', None, strObject)

    def is_object_solid(self, str_object):
        """

        Verifies that an object is a closed, solid object.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectSolid', None, strObject)

    def is_object_valid(self, str_object):
        """

        Verifies that an object's geometry is valid and without error.

        Parameters

        strObject : Required, String, The identifier of an object

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectValid', None, strObject)

    def is_visible_in_view(self, str_object, str_view):
        """

        Verifies that an object is visible in a view.

        Parameters

        strObject : Required, String, The identifier of an object
        strView : Optional, String, The title of the view

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsVisibleInView', None, strObject, strView)

    def lock_object(self, str_object):
        """

        Locks a single object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strObject : Required, String, The identifier of the object to lock

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LockObject', None, strObject)

    def lock_objects(self, arr_objects):
        """

        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to lock

        Returns

        Number : The number of objects locked if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LockObjects', None, arrObjects)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def mirror_object(self, str_object, arr_start_pt, arr_end_pt, bln_copy):
        """

        Mirrors a single object.

        Parameters

        strObject : Required, String, The identifier of the object to mirror
        arrStartPt : Required, Array, The start of the mirror plane
        arrEndPt : Required, Array, The end of the mirror plane
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : The identifier of the mirrored object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MirrorObject', None, strObject, arrStartPt, arrEndPt, blnCopy)

    def mirror_objects(self, arr_objects, arr_start_pt, arr_end_pt, bln_copy):
        """

        Mirrors one or more objects.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to mirror
        arrStartPt : Required, Array, The start of the mirror plane
        arrEndPt : Required, Array, The end of the mirror plane
        blnCopy : Optional, Boolean, Copy the objects

        Returns

        String : An array of strings identifying the mirrored objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MirrorObjects', None, arrObjects, arrStartPt, arrEndPt, blnCopy)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_description(self, str_object):
        """

        Returns a short text description of an object.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        String : A short text description of the object is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectDescription', None, strObject)

    def object_dump(self, str_object, int_type):
        """

        Returns a detailed description of an object.

        Parameters

        strObject : Required, String, The identifier of the object
        intType : Optional, The type of dump, The acceptable values are as follows:

        Returns

        String : A detailed description of the object is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectDump', None, strObject, intType)

    def object_groups(self, str_object):
        """

        Returns all of the group names that an object is assigned.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Array : An array of all group names for the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectGroups', None, strObject)

    def object_has_mesh(self, str_object):
        """

        Verifies that an object has custom render mesh parameters.

        Parameters

        strObject : Required, Object, The identifier of a meshable object

        Returns

        Boolean : True of the object has custom render mesh parameters, False otherwise.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectHasMesh', None, strObject)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_layout(self, str_object, str_layout, bln_return_name):
        """

        Returns or changes the layout or model space of an object.

        Parameters

        strObject : Required, String, The identifier of the object
        strLayout : Optional, String, To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view
        blnReturnName : Optional, Boolean, If True (default), then the name, or title, of the page layout view is returned

        Returns

        String : If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.
        String : If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectLayout', None, strObject, strLayout, blnReturnName)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_material_index(self, str_object):
        """

        If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Number : The rendering material index if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMaterialIndex', None, strObject)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_mesh_density(self, str_object, dbl_density):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblDensity : Optional, Number, The render mesh density, which is a number between 0

        Returns

        Boolean : If dblDensity is not specified, the current render mesh density if successful.
        Boolean : If dblDensity is specified, the previous render mesh density if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshDensity', None, strObject, dblDensity)

    def object_mesh_max_angle(self, str_object, dbl_angle):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblAngle : Optional, Number, The render mesh maximum angle in degrees

        Returns

        Boolean : If dblAngle is not specified, the current render mesh maximum angle if successful.
        Boolean : If dblAngle is specified, the previous render mesh maximum angle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMaxAngle', None, strObject, dblAngle)

    def object_mesh_max_aspect_ratio(self, str_object, dbl_ratio):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblRatio : Optional, Number, The render mesh maximum aspect ratio

        Returns

        Boolean : If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
        Boolean : If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMaxAspectRatio', None, strObject, dblRatio)

    def object_mesh_max_dist_edge_to_srf(self, str_object, dbl_distance):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblDistance : Optional, Number, The render mesh maximum distance, edge to surface

        Returns

        Boolean : If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
        Boolean : If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMaxDistEdgeToSrf', None, strObject, dblDistance)

    def object_mesh_max_edge_length(self, str_object, dbl_length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblLength : Optional, Number, The render mesh maximum edge length

        Returns

        Boolean : If dblLength is not specified, the current render mesh maximum edge length if successful.
        Boolean : If dblLength is specified, the previous render mesh maximum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMaxEdgeLength', None, strObject, dblLength)

    def object_mesh_min_edge_length(self, str_object, dbl_length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        dblLength : Optional, Number, The render mesh minimum edge length

        Returns

        Boolean : If dblLength is not specified, the current render mesh minimum edge length if successful.
        Boolean : If dblLength is specified, the previous render mesh minimum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMinEdgeLength', None, strObject, dblLength)

    def object_mesh_min_initial_grid_quads(self, str_object, int_quads):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        intQuads : Optional, Number, The render mesh minimum initial grid quads

        Returns

        Boolean : If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
        Boolean : If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshMinInitialGridQuads', None, strObject, intQuads)

    def object_mesh_quality(self, str_object, int_quality):
        """

        Returns or sets the render mesh quality of an object's custom render mesh parameters.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        intQuality : Optional, Number, The render mesh quality, either:

        Returns

        Boolean : If intQuality is not specified, the current render mesh quality if successful.
        Boolean : If intQuality is specified, the previous render mesh quality if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshQuality', None, strObject, intQuality)

    def object_mesh_settings(self, str_object, int_settings):
        """

        Returns or sets the render mesh settings of an object's custom render mesh parameters.

        Parameters

        strObject : Required, Object, The identifier of an object that has custom render mesh parameters
        intSettings : Optional, Number, The render mesh settings, which is a bit-coded number that allows or disallows certain features

        Returns

        Boolean : If intSettings is not specified, the current render mesh settings if successful.
        Boolean : If intSettings is specified, the previous render mesh settings if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectMeshSettings', None, strObject, intSettings)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_names(self, arr_objects, arr_names):
        """

        Returns or modifies the user-definable name of one or more objects.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects
        arrNames : Optional, Array, An array of strings identifying the new user-definable names

        Returns

        Array : If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        Array : If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectNames', None, arrObjects, arrNames)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_top_group(self, str_object):
        """

        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        String : The top most group name of the object if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectTopGroup', None, strObject)

    def object_type(self, str_object):
        """

        Returns the object type.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Number : The object type if successful.  The valid object types are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectType', None, strObject)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def orient_object(self, str_object, arr_reference, arr_target, int_flags):
        """

        Orients a single object based on input points.

        Parameters

        strObject : Required, String, The identifier of the object to orient
        arrReference : Required, Array, An array of 3-D reference points
        arrTarget : Required, Array, An array of 3-D target points
        intFlags : Optional, Number, The orient flags

        Returns

        String : The identifier of the oriented object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'OrientObject', None, strObject, arrReference, arrTarget, intFlags)

    def orient_objects(self, arr_objects, arr_reference, arr_target, int_flags):
        """

        Orients one or more objects based on input points.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to orient
        arrReference : Required, Array, An array of 3-D reference points
        arrTarget : Required, Array, An array of 3-D target points
        intFlags : Optional, Number, The orient flags

        Returns

        Array : An array of strings identifying the oriented objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'OrientObjects', None, arrObjects, arrReference, arrTarget, intFlags)

    def remap_object(self, str_object, arr_src_plane, arr_dst_plane, bln_copy):
        """

        Remqps a single object from one plane, or coordinate system, to another.

        Parameters

        strObject : Required, String, The identifier of the object to remap
        arrSrcPlane : Required, Array, The source plane to transform from
        arrDstPlane : Required, Array, The destination plane to transform to
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : The identifier of the remapped object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemapObject', None, strObject, arrSrcPlane, arrDstPlane, blnCopy)

    def remap_objects(self, arr_object, arr_src_plane, arr_dst_plane, bln_copy):
        """

        Remqps one or more objects from one plane, or coordinate system, to another.

        Parameters

        arrObject : Required, Array, The identifiers of the objects to remap
        arrSrcPlane : Required, Array, The source plane to transform from
        arrDstPlane : Required, Array, The destination plane to transform to
        blnCopy : Optional, Boolean, Copy the object

        Returns

        Array : An array of strings identifying the remapped objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemapObjects', None, arrObject, arrSrcPlane, arrDstPlane, blnCopy)

    def rotate_object(self, str_object, arr_point, dbl_angle, arr_axis, bln_copy):
        """

        Rotates a single object. Rotation is based on the active construction plane.

        Parameters

        strObject : Required, String, The identifier of the object to rotate
        arrPoint : Required, Array, The 3-D center point of the rotation
        dblAngle : Required, Number, The rotation angle in degrees
        arrAxis : Optional, Array, A 3-D vector that identifies the axis of rotation
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : The identifier of the rotated object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RotateObject', None, strObject, arrPoint, dblAngle, arrAxis, blnCopy)

    def rotate_objects(self, arr_objects, arr_point, dbl_angle, arr_axis, bln_copy):
        """

        Rotates one or more objects. Rotation is based on the active construction plane.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to rotate
        arrPoint : Required, Array, The 3-D center point of the rotation
        dblAngle : Required, Number, The rotation angle in degrees
        arrAxis : Optional, Array, A 3-D vector that identifies the axis of rotation
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : An array of strings identifying the rotated objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RotateObjects', None, arrObjects, arrPoint, dblAngle, arrAxis, blnCopy)

    def scale_object(self, str_object, arr_origin, arr_scale, bln_copy):
        """

        Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

        Parameters

        strObject : Required, String, The identifier of the object to scale
        arrOrigin : Required, Array, The origin of the scale transformation
        arrScale : Required, Array, An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : The identifier of the scaled object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ScaleObject', None, strObject, arrOrigin, arrScale, blnCopy)

    def scale_objects(self, arr_objects, arr_origin, arr_scale, bln_copy):
        """

        Scales one or more objects. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to scale
        arrOrigin : Required, Array, The origin of the scale transformation
        arrScale : Required, Array, An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply
        blnCopy : Optional, Boolean, Copy the objects

        Returns

        Array : An array of strings identifying the scaled objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ScaleObjects', None, arrObjects, arrOrigin, arrScale, blnCopy)

    def select_object(self, str_object):
        """

        Selects a single object.

        Parameters

        strObject : Required, String, The identifier of the object to select

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SelectObject', None, strObject)

    def select_objects(self, arr_objects):
        """

        Selects one or more objects.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to select

        Returns

        Number : The number of objects selected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SelectObjects', None, arrObjects)

    def shear_object(self, str_object, arr_origin, arr_ref_pt, arr_scale, bln_copy):
        """

        Performs a shear transformation on a single object. Transformation is based on the active construction plane.

        Parameters

        strObject : Required, String, The identifier of the object to shear
        arrOrigin : Required, Array, The origin of the shear transformation
        arrRefPt : Required, Array, The reference point of the shear transformation
        arrScale : Required, Number, An angle in degrees of the shear transformation, where -90
        blnCopy : Optional, Boolean, Copy the object

        Returns

        String : The identifier of the sheared object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShearObject', None, strObject, arrOrigin, arrRefPt, arrScale, blnCopy)

    def shear_objects(self, arr_objects, arr_origin, arr_ref_pt, arr_scale, bln_copy):
        """

        Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to shear
        arrOrigin : Required, Array, The origin of the shear transformation
        arrRefPt : Required, Array, The reference point of the shear transformation
        arrScale : Required, Number, An angle in degrees of the shear transformation, where -90
        blnCopy : Optional, Boolean, Copy the objects

        Returns

        Array : An array of strings identifying the scaled objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShearObjects', None, arrObjects, arrOrigin, arrRefPt, arrScale, blnCopy)

    def show_object(self, str_object):
        """

        Shows a previously hidden object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strObject : Required, String, The identifier of the object to show

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShowObject', None, strObject)

    def show_objects(self, arr_objects):
        """

        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to show

        Returns

        Number : The number of objects shown if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShowObjects', None, arrObjects)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def unlock_object(self, str_object):
        """

        Unlocks a previously locked object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strObject : Required, String, The identifier of the object to unlock

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnlockObject', None, strObject)

    def unlock_objects(self, arr_objects):
        """

        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to unlock

        Returns

        Number : The number of objects unlocked if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnlockObjects', None, arrObjects)

    def unselect_object(self, str_object):
        """

        Unselects a single selected object.

        Parameters

        strObject : Required, String, The identifier of the object to unselect

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnselectObject', None, strObject)

    def unselect_objects(self, arr_objects):
        """

        Unselects one or more selected objects.

        Parameters

        arrObjects : Required, Array, An array of strings identifying the objects to unselect

        Returns

        Number : The number of objects unselected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnselectObjects', None, arrObjects)

