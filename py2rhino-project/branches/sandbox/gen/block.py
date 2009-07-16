# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Block(DispatchBaseClass):



    def block_container_count(self, block):
        """

        Returns the number of block definitions that contain a specified block definition.

        Parameters

        Block : Required, String, str

        Returns

        Number : The number of block definitions that contain the specified block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(411, 1, (12, 0), ((12, 0)), u'BlockContainerCount', None, block)

    def block_containers(self, block):
        """

        Returns the names of the block definitions that contain a specified block definition.

        Parameters

        Block : Required, String, str

        Returns

        Array : An array of block definition names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(412, 1, (12, 0), ((12, 0)), u'BlockContainers', None, block)

    def block_count(self):
        """

        Returns the number of block definitions in the document.

        No parameters

        Returns

        Number : The number of block definitions in the document.
        Null : On error.

        """

        return self._ApplyTypes_(397, 1, (12, 0), (), u'BlockCount', None, )

    def block_description(self, block, text):
        """

        Returns or sets the description of a block definition.

        Parameters

        Block : Required, String, str
        Text : Optional, String, str

        Returns

        String : If a description is not specified,  the current description if successful.
        String : If a description is specified, the previous description if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(400, 1, (12, 0), ((12, 0), (12, 0)), u'BlockDescription', None, block, text)

    def block_instance_count(self, block):
        """

        Counts the number of instances of the block in the document.  Nested instances are not included in the count.

        Parameters

        Block : Required, String, str

        Returns

        Number : The number of instances of the block in the document if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(404, 1, (12, 0), ((12, 0)), u'BlockInstanceCount', None, block)

    def block_instance_insert_point(self, object):
        """

        Returns the insertion point of a block instance.

        Parameters

        Object : Required, String, str

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(413, 1, (12, 0), ((12, 0)), u'BlockInstanceInsertPoint', None, object)

    def block_instance_name(self, object):
        """

        Returns the block name of a block instance.

        Parameters

        Object : Required, String, str

        Returns

        String : The block name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(571, 1, (12, 0), ((12, 0)), u'BlockInstanceName', None, object)

    def block_instance_xform(self, object):
        """

        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

        Parameters

        Object : Required, String, str

        Returns

        Array : A transformation matrix (4x4 array of numbers) if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(415, 1, (12, 0), ((12, 0)), u'BlockInstanceXform', None, object)

    def block_instances(self, block):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def block_names(self, sort):
        """

        Returns the names of all block definitions in the document.

        Parameters

        Sort : Optional, Boolean, bln

        Returns

        Array : An array of block definition names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(396, 1, (12, 0), ((12, 0)), u'BlockNames', None, sort)

    def block_object_count(self, block):
        """

        Returns the number of objects that make up a block definition.

        Parameters

        Block : Required, String, str

        Returns

        Number : The number of objects that make up the block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(416, 1, (12, 0), ((12, 0)), u'BlockObjectCount', None, block)

    def block_objects(self, block):
        """

        Returns the identifiers of the objects that make up a block definition.

        Parameters

        Block : Required, String, str

        Returns

        Array : An array of strings identifying the objects that make up a block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(417, 1, (12, 0), ((12, 0)), u'BlockObjects', None, block)

    def block_path(self, block):
        """

        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

        Parameters

        Block : Required, String, str

        Returns

        String : The path to the linked block file is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(408, 1, (12, 0), ((12, 0)), u'BlockPath', None, block)

    def block_u_r_l(self, block, u_r_l):
        """

        Returns or sets the URL of a block definition.

        Parameters

        Block : Required, String, str
        URL : Optional, String, str

        Returns

        String : If a URL is not specified,  the current URL if successful.
        String : If a URL is specified, the previous URL if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(402, 1, (12, 0), ((12, 0), (12, 0)), u'BlockURL', None, block, u_r_l)

    def block_u_r_l_tag(self, block, u_r_l):
        """

        Returns or sets the URL tag, or description, of a block definition.

        Parameters

        Block : Required, String, str
        URL : Optional, String, str

        Returns

        String : If a URL tag is not specified,  the current URL tag if successful.
        String : If a URL tag is specified, the previous URL tag if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(403, 1, (12, 0), ((12, 0), (12, 0)), u'BlockURLTag', None, block, u_r_l)

    def delete_block(self, block):
        """

        Deletes a block definition and all of it's inserted instances.

        Parameters

        Block : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(418, 1, (12, 0), ((12, 0)), u'DeleteBlock', None, block)

    def explode_block_instance(self, object):
        """

        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

        Parameters

        Object : Required, String, str

        Returns

        Array : An array of strings identifying the newly exploded objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(419, 1, (12, 0), ((12, 0)), u'ExplodeBlockInstance', None, object)

    def insert_block(self, name, point, scale, angle, normal, xform):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_block(self, block):
        """

        Verifies the existence of a block definition in the document.

        Parameters

        Block : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(398, 1, (12, 0), ((12, 0)), u'IsBlock', None, block)

    def is_block_embedded(self, block):
        """

        Verifies that a block definition is embedded, or linked, from an external file.

        Parameters

        Block : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(405, 1, (12, 0), ((12, 0)), u'IsBlockEmbedded', None, block)

    def is_block_in_use(self, block, where):
        """

        Verifies that a block definition is being used by an inserted instance.

        Parameters

        Block : Required, String, str
        Where : Optional, Number, int

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(406, 1, (12, 0), ((12, 0), (12, 0)), u'IsBlockInUse', None, block, where)

    def is_block_instance(self, object):
        """

        Verifies an object is a block instance.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(420, 1, (12, 0), ((12, 0)), u'IsBlockInstance', None, object)

    def is_block_reference(self, block):
        """

        Verifies that a block definition is from a reference file.

        Parameters

        Block : Required, String, str

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(407, 1, (12, 0), ((12, 0)), u'IsBlockReference', None, block)

    def rename_block(self, old_block, new_block):
        """

        Renames an existing block definition.

        Parameters

        OldBlock : Required, String, str
        NewBlock : Required, String, str

        Returns

        String : The new block definition name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(399, 1, (12, 0), ((12, 0), (12, 0)), u'RenameBlock', None, old_block, new_block)

