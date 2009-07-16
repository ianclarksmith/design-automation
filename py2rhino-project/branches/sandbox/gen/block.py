# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Block(DispatchBaseClass):



    def block_container_count(self, str_block):
        """

        Returns the number of block definitions that contain a specified block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Number : The number of block definitions that contain the specified block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockContainerCount', None, strBlock)

    def block_containers(self, str_block):
        """

        Returns the names of the block definitions that contain a specified block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Array : An array of block definition names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockContainers', None, strBlock)

    def block_count(self):
        """

        Returns the number of block definitions in the document.

        No parameters

        Returns

        Number : The number of block definitions in the document.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockCount', None, )

    def block_description(self, str_block, str_text):
        """

        Returns or sets the description of a block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition
        strText : Optional, String, The new description

        Returns

        String : If a description is not specified,  the current description if successful.
        String : If a description is specified, the previous description if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockDescription', None, strBlock, strText)

    def block_instance_count(self, str_block):
        """

        Counts the number of instances of the block in the document.  Nested instances are not included in the count.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Number : The number of instances of the block in the document if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceCount', None, strBlock)

    def block_instance_insert_point(self, str_object):
        """

        Returns the insertion point of a block instance.

        Parameters

        strObject : Required, String, The identifier of an existing block insertion object

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceInsertPoint', None, strObject)

    def block_instance_name(self, str_object):
        """

        Returns the block name of a block instance.

        Parameters

        strObject : Required, String, The identifier of an existing block insertion object

        Returns

        String : The block name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceName', None, strObject)

    def block_instance_xform(self, str_object):
        """

        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

        Parameters

        strObject : Required, String, The identifier of an existing block insertion object

        Returns

        Array : A transformation matrix (4x4 array of numbers) if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockInstanceXform', None, strObject)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def block_names(self, bln_sort):
        """

        Returns the names of all block definitions in the document.

        Parameters

        blnSort : Optional, Boolean, Return a sorted array of block definition names

        Returns

        Array : An array of block definition names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockNames', None, blnSort)

    def block_object_count(self, str_block):
        """

        Returns the number of objects that make up a block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Number : The number of objects that make up the block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockObjectCount', None, strBlock)

    def block_objects(self, str_block):
        """

        Returns the identifiers of the objects that make up a block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Array : An array of strings identifying the objects that make up a block definition if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockObjects', None, strBlock)

    def block_path(self, str_block):
        """

        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        String : The path to the linked block file is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockPath', None, strBlock)

    def block_u_r_l(self, str_block, str_u_r_l):
        """

        Returns or sets the URL of a block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition
        strURL : Optional, String, The new URL

        Returns

        String : If a URL is not specified,  the current URL if successful.
        String : If a URL is specified, the previous URL if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockURL', None, strBlock, strURL)

    def block_u_r_l_tag(self, str_block, str_u_r_l):
        """

        Returns or sets the URL tag, or description, of a block definition.

        Parameters

        strBlock : Required, String, The name of an existing block definition
        strURL : Optional, String, The new URL tag

        Returns

        String : If a URL tag is not specified,  the current URL tag if successful.
        String : If a URL tag is specified, the previous URL tag if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BlockURLTag', None, strBlock, strURL)

    def delete_block(self, str_block):
        """

        Deletes a block definition and all of it's inserted instances.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteBlock', None, strBlock)

    def explode_block_instance(self, str_object):
        """

        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

        Parameters

        strObject : Required, String, The identifier of an existing block definition

        Returns

        Array : An array of strings identifying the newly exploded objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExplodeBlockInstance', None, strObject)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_block(self, str_block):
        """

        Verifies the existence of a block definition in the document.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlock', None, strBlock)

    def is_block_embedded(self, str_block):
        """

        Verifies that a block definition is embedded, or linked, from an external file.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockEmbedded', None, strBlock)

    def is_block_in_use(self, str_block, int_where):
        """

        Verifies that a block definition is being used by an inserted instance.

        Parameters

        strBlock : Required, String, The name of an existing block definition
        intWhere : Optional, Number, Where to look, where:

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockInUse', None, strBlock, intWhere)

    def is_block_instance(self, str_object):
        """

        Verifies an object is a block instance.

        Parameters

        strObject : Required, String, The identifier of an existing block definition

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockInstance', None, strObject)

    def is_block_reference(self, str_block):
        """

        Verifies that a block definition is from a reference file.

        Parameters

        strBlock : Required, String, The name of an existing block definition

        Returns

        Boolean : True or false indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBlockReference', None, strBlock)

    def rename_block(self, str_old_block, str_new_block):
        """

        Renames an existing block definition.

        Parameters

        strOldBlock : Required, String, The name of an existing block definition
        strNewBlock : Required, String, The new block definition name

        Returns

        String : The new block definition name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RenameBlock', None, strOldBlock, strNewBlock)

