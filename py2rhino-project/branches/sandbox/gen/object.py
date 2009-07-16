# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Object(DispatchBaseClass):



    def add_object_mesh(self, object, quality, enable):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Quality : Optional, Number, int
        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(866, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddObjectMesh', None, object, quality, enable)

    def box_morph_object(self, object, objects, box_points, copy):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def copy_object(self, object, start, end, translation):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def copy_objects(self, objects, start, end, translation):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def delete_object(self, object):
        """

        Deletes a single object from the document.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(185, 1, (12, 0), ((12, 0)), u'DeleteObject', None, object)

    def delete_objects(self, objects):
        """

        Deletes one or more objects from the document.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects deleted if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(186, 1, (12, 0), ((12, 0)), u'DeleteObjects', None, objects)

    def enable_object_mesh(self, objects, enable):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Objects : Required, Object, arr
        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Boolean : If blnEnable is not specified, then the current enabled/disabled state if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(856, 1, (12, 0), ((12, 0), (12, 0)), u'EnableObjectMesh', None, objects, enable)

    def flash_object(self, object, objects, style):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def hide_object(self, object):
        """

        Hides a single object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(187, 1, (12, 0), ((12, 0)), u'HideObject', None, object)

    def hide_objects(self, objects):
        """

        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects hidden if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(303, 1, (12, 0), ((12, 0)), u'HideObjects', None, objects)

    def is_layout_object(self, object):
        """

        Verifies that an object is in either page layout space or model space.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(919, 1, (12, 0), ((12, 0)), u'IsLayoutObject', None, object)

    def is_object(self, object):
        """

        Verifies the existence of an object.

        Parameters

        Object : Required, String, str

        No returns


        """

        return self._ApplyTypes_(46, 1, (12, 0), ((12, 0)), u'IsObject', None, object)

    def is_object_hidden(self, object):
        """

        Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(47, 1, (12, 0), ((12, 0)), u'IsObjectHidden', None, object)

    def is_object_in_box(self, object, box, mode):
        """

        Verifies an object's bounding box is inside of another bounding box.

        Parameters

        Object : Required, String, str
        Box : Required, Array, arr
        Mode : Optional, Boolean, bln

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(799, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'IsObjectInBox', None, object, box, mode)

    def is_object_in_group(self, object, group):
        """

        Verifies that an object is a member of a specified group.

        Parameters

        Object : Required, String, str
        Group : Optional, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(188, 1, (12, 0), ((12, 0), (12, 0)), u'IsObjectInGroup', None, object, group)

    def is_object_locked(self, object):
        """

        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(48, 1, (12, 0), ((12, 0)), u'IsObjectLocked', None, object)

    def is_object_normal(self, object):
        """

        Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(49, 1, (12, 0), ((12, 0)), u'IsObjectNormal', None, object)

    def is_object_reference(self, object):
        """

        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(271, 1, (12, 0), ((12, 0)), u'IsObjectReference', None, object)

    def is_object_selectable(self, object):
        """

        Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(307, 1, (12, 0), ((12, 0)), u'IsObjectSelectable', None, object)

    def is_object_selected(self, object):
        """

        Verifies that an object is currently selected.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(50, 1, (12, 0), ((12, 0)), u'IsObjectSelected', None, object)

    def is_object_solid(self, object):
        """

        Verifies that an object is a closed, solid object.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(189, 1, (12, 0), ((12, 0)), u'IsObjectSolid', None, object)

    def is_object_valid(self, object):
        """

        Verifies that an object's geometry is valid and without error.

        Parameters

        Object : Required, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(522, 1, (12, 0), ((12, 0)), u'IsObjectValid', None, object)

    def is_visible_in_view(self, object, view):
        """

        Verifies that an object is visible in a view.

        Parameters

        Object : Required, String, str
        View : Optional, String, str

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(727, 1, (12, 0), ((12, 0), (12, 0)), u'IsVisibleInView', None, object, view)

    def lock_object(self, object):
        """

        Locks a single object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(190, 1, (12, 0), ((12, 0)), u'LockObject', None, object)

    def lock_objects(self, objects):
        """

        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects locked if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(304, 1, (12, 0), ((12, 0)), u'LockObjects', None, objects)

    def match_object_attributes(self, target, targets, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def mirror_object(self, object, start_pt, end_pt, copy):
        """

        Mirrors a single object.

        Parameters

        Object : Required, String, str
        StartPt : Required, Array, arr
        EndPt : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : The identifier of the mirrored object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(589, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'MirrorObject', None, object, start_pt, end_pt, copy)

    def mirror_objects(self, objects, start_pt, end_pt, copy):
        """

        Mirrors one or more objects.

        Parameters

        Objects : Required, Array, arr
        StartPt : Required, Array, arr
        EndPt : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : An array of strings identifying the mirrored objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(590, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'MirrorObjects', None, objects, start_pt, end_pt, copy)

    def move_object(self, object, start, end, translation):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def move_objects(self, objects, start, end, translation):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_color(self, object, objects, color):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_color_source(self, object, objects, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_description(self, object):
        """

        Returns a short text description of an object.

        Parameters

        Object : Required, String, str

        Returns

        String : A short text description of the object is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(470, 1, (12, 0), ((12, 0)), u'ObjectDescription', None, object)

    def object_dump(self, object, type):
        """

        Returns a detailed description of an object.

        Parameters

        Object : Required, String, str
        Type : Optional, The type of dump, int

        Returns

        String : A detailed description of the object is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(705, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectDump', None, object, type)

    def object_groups(self, object):
        """

        Returns all of the group names that an object is assigned.

        Parameters

        Object : Required, String, str

        Returns

        Array : An array of all group names for the object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(193, 1, (12, 0), ((12, 0)), u'ObjectGroups', None, object)

    def object_has_mesh(self, object):
        """

        Verifies that an object has custom render mesh parameters.

        Parameters

        Object : Required, Object, str

        Returns

        Boolean : True of the object has custom render mesh parameters, False otherwise.
        Null : On error.

        """

        return self._ApplyTypes_(867, 1, (12, 0), ((12, 0)), u'ObjectHasMesh', None, object)

    def object_layer(self, object, objects, layer):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_layout(self, object, layout, return_name):
        """

        Returns or changes the layout or model space of an object.

        Parameters

        Object : Required, String, str
        Layout : Optional, String, str
        ReturnName : Optional, Boolean, bln

        Returns

        String : If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.
        String : If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(924, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ObjectLayout', None, object, layout, return_name)

    def object_linetype(self, object, objects, layer):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_linetype_source(self, object, objects, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_material_index(self, object):
        """

        If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.

        Parameters

        Object : Required, String, str

        Returns

        Number : The rendering material index if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(194, 1, (12, 0), ((12, 0)), u'ObjectMaterialIndex', None, object)

    def object_material_source(self, object, objects, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_mesh_density(self, object, density):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Density : Optional, Number, dbl

        Returns

        Boolean : If dblDensity is not specified, the current render mesh density if successful.
        Boolean : If dblDensity is specified, the previous render mesh density if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(858, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshDensity', None, object, density)

    def object_mesh_max_angle(self, object, angle):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Angle : Optional, Number, dbl

        Returns

        Boolean : If dblAngle is not specified, the current render mesh maximum angle if successful.
        Boolean : If dblAngle is specified, the previous render mesh maximum angle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(859, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMaxAngle', None, object, angle)

    def object_mesh_max_aspect_ratio(self, object, ratio):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Ratio : Optional, Number, dbl

        Returns

        Boolean : If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
        Boolean : If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(860, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMaxAspectRatio', None, object, ratio)

    def object_mesh_max_dist_edge_to_srf(self, object, distance):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Distance : Optional, Number, dbl

        Returns

        Boolean : If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
        Boolean : If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(863, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMaxDistEdgeToSrf', None, object, distance)

    def object_mesh_max_edge_length(self, object, length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Length : Optional, Number, dbl

        Returns

        Boolean : If dblLength is not specified, the current render mesh maximum edge length if successful.
        Boolean : If dblLength is specified, the previous render mesh maximum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(862, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMaxEdgeLength', None, object, length)

    def object_mesh_min_edge_length(self, object, length):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Length : Optional, Number, dbl

        Returns

        Boolean : If dblLength is not specified, the current render mesh minimum edge length if successful.
        Boolean : If dblLength is specified, the previous render mesh minimum edge length if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(861, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMinEdgeLength', None, object, length)

    def object_mesh_min_initial_grid_quads(self, object, quads):
        """

        For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters

        Object : Required, Object, str
        Quads : Optional, Number, int

        Returns

        Boolean : If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
        Boolean : If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(864, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshMinInitialGridQuads', None, object, quads)

    def object_mesh_quality(self, object, quality):
        """

        Returns or sets the render mesh quality of an object's custom render mesh parameters.

        Parameters

        Object : Required, Object, str
        Quality : Optional, Number, int

        Returns

        Boolean : If intQuality is not specified, the current render mesh quality if successful.
        Boolean : If intQuality is specified, the previous render mesh quality if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(857, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshQuality', None, object, quality)

    def object_mesh_settings(self, object, settings):
        """

        Returns or sets the render mesh settings of an object's custom render mesh parameters.

        Parameters

        Object : Required, Object, str
        Settings : Optional, Number, int

        Returns

        Boolean : If intSettings is not specified, the current render mesh settings if successful.
        Boolean : If intSettings is specified, the previous render mesh settings if successful.
        Null : If the object does not have custom render mesh parameters, or on error.

        """

        return self._ApplyTypes_(865, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectMeshSettings', None, object, settings)

    def object_name(self, object, objects, name):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_names(self, objects, names):
        """

        Returns or modifies the user-definable name of one or more objects.

        Parameters

        Objects : Required, Array, arr
        Names : Optional, Array, arr

        Returns

        Array : If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        Array : If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(639, 1, (12, 0), ((12, 0), (12, 0)), u'ObjectNames', None, objects, names)

    def object_print_color(self, object, objects, color):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_print_color_source(self, object, objects, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_print_width(self, object, objects, width):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_print_width_source(self, object, objects, source):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def object_top_group(self, object):
        """

        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.

        Parameters

        Object : Required, String, str

        Returns

        String : The top most group name of the object if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(197, 1, (12, 0), ((12, 0)), u'ObjectTopGroup', None, object)

    def object_type(self, object):
        """

        Returns the object type.

        Parameters

        Object : Required, String, str

        Returns

        Number : The object type if successful.  The valid object types are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(198, 1, (12, 0), ((12, 0)), u'ObjectType', None, object)

    def object_u_r_l(self, object, objects, u_r_l):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def orient_object(self, object, reference, target, flags):
        """

        Orients a single object based on input points.

        Parameters

        Object : Required, String, str
        Reference : Required, Array, arr
        Target : Required, Array, arr
        Flags : Optional, Number, int

        Returns

        String : The identifier of the oriented object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(390, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'OrientObject', None, object, reference, target, flags)

    def orient_objects(self, objects, reference, target, flags):
        """

        Orients one or more objects based on input points.

        Parameters

        Objects : Required, Array, arr
        Reference : Required, Array, arr
        Target : Required, Array, arr
        Flags : Optional, Number, int

        Returns

        Array : An array of strings identifying the oriented objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(391, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'OrientObjects', None, objects, reference, target, flags)

    def remap_object(self, object, src_plane, dst_plane, copy):
        """

        Remqps a single object from one plane, or coordinate system, to another.

        Parameters

        Object : Required, String, str
        SrcPlane : Required, Array, arr
        DstPlane : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : The identifier of the remapped object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(655, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'RemapObject', None, object, src_plane, dst_plane, copy)

    def remap_objects(self, object, src_plane, dst_plane, copy):
        """

        Remqps one or more objects from one plane, or coordinate system, to another.

        Parameters

        Object : Required, Array, arr
        SrcPlane : Required, Array, arr
        DstPlane : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        Array : An array of strings identifying the remapped objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(656, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'RemapObjects', None, object, src_plane, dst_plane, copy)

    def rotate_object(self, object, point, angle, axis, copy):
        """

        Rotates a single object. Rotation is based on the active construction plane.

        Parameters

        Object : Required, String, str
        Point : Required, Array, arr
        Angle : Required, Number, dbl
        Axis : Optional, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : The identifier of the rotated object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(392, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'RotateObject', None, object, point, angle, axis, copy)

    def rotate_objects(self, objects, point, angle, axis, copy):
        """

        Rotates one or more objects. Rotation is based on the active construction plane.

        Parameters

        Objects : Required, Array, arr
        Point : Required, Array, arr
        Angle : Required, Number, dbl
        Axis : Optional, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : An array of strings identifying the rotated objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(393, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'RotateObjects', None, objects, point, angle, axis, copy)

    def scale_object(self, object, origin, scale, copy):
        """

        Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

        Parameters

        Object : Required, String, str
        Origin : Required, Array, arr
        Scale : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        String : The identifier of the scaled object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(585, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ScaleObject', None, object, origin, scale, copy)

    def scale_objects(self, objects, origin, scale, copy):
        """

        Scales one or more objects. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

        Parameters

        Objects : Required, Array, arr
        Origin : Required, Array, arr
        Scale : Required, Array, arr
        Copy : Optional, Boolean, bln

        Returns

        Array : An array of strings identifying the scaled objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(586, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ScaleObjects', None, objects, origin, scale, copy)

    def select_object(self, object):
        """

        Selects a single object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(200, 1, (12, 0), ((12, 0)), u'SelectObject', None, object)

    def select_objects(self, objects):
        """

        Selects one or more objects.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects selected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(298, 1, (12, 0), ((12, 0)), u'SelectObjects', None, objects)

    def shear_object(self, object, origin, ref_pt, scale, copy):
        """

        Performs a shear transformation on a single object. Transformation is based on the active construction plane.

        Parameters

        Object : Required, String, str
        Origin : Required, Array, arr
        RefPt : Required, Array, arr
        Scale : Required, Number, arr
        Copy : Optional, Boolean, bln

        Returns

        String : The identifier of the sheared object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(587, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'ShearObject', None, object, origin, ref_pt, scale, copy)

    def shear_objects(self, objects, origin, ref_pt, scale, copy):
        """

        Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.

        Parameters

        Objects : Required, Array, arr
        Origin : Required, Array, arr
        RefPt : Required, Array, arr
        Scale : Required, Number, arr
        Copy : Optional, Boolean, bln

        Returns

        Array : An array of strings identifying the scaled objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(588, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'ShearObjects', None, objects, origin, ref_pt, scale, copy)

    def show_object(self, object):
        """

        Shows a previously hidden object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(201, 1, (12, 0), ((12, 0)), u'ShowObject', None, object)

    def show_objects(self, objects):
        """

        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects shown if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(305, 1, (12, 0), ((12, 0)), u'ShowObjects', None, objects)

    def transform_object(self, object, matrix, copy):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def transform_objects(self, objects, matrix, copy):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def unlock_object(self, object):
        """

        Unlocks a previously locked object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(202, 1, (12, 0), ((12, 0)), u'UnlockObject', None, object)

    def unlock_objects(self, objects):
        """

        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects unlocked if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(306, 1, (12, 0), ((12, 0)), u'UnlockObjects', None, objects)

    def unselect_object(self, object):
        """

        Unselects a single selected object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(299, 1, (12, 0), ((12, 0)), u'UnselectObject', None, object)

    def unselect_objects(self, objects):
        """

        Unselects one or more selected objects.

        Parameters

        Objects : Required, Array, arr

        Returns

        Number : The number of objects unselected if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(300, 1, (12, 0), ((12, 0)), u'UnselectObjects', None, objects)

