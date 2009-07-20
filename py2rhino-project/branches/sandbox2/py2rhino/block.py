# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Block(IRhinoScript):



    def block_container_count(self, block):
        """        
        Returns the number of block definitions that contain a specified block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        number
        The number of block definitions that contain the specified block definition if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(411, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockContainerCount", None, block)

    def block_containers(self, block):
        """        
        Returns the names of the block definitions that contain a specified block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        array
        An array of block definition names if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(412, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockContainers", None, block)

    def block_count(self):
        """        
        Returns the number of block definitions in the document.
    
        No parameters

        Returns
        =======

        number
        The number of block definitions in the document.

        null
        On error.

        """

        return self._ApplyTypes_(397, 1, (VT_VARIANT, 0), (), u"BlockCount", None, )

    def block_description(self, block, text):
        """        
        Returns or sets the description of a block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        text, String, Optional        
        The new description.  If omitted, the current description is returned.
            
        Returns
        =======

        string
        If a description is not specified,  the current description if successful.

        string
        If a description is specified, the previous description if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(400, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"BlockDescription", None, block, text)

    def block_instance_count(self, block):
        """        
        Counts the number of instances of the block in the document.  Nested instances are not included in the count.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        number
        The number of instances of the block in the document if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(404, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockInstanceCount", None, block)

    def block_instance_insert_point(self, object):
        """        
        Returns the insertion point of a block instance.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an existing block insertion object.
            
        Returns
        =======

        array
        A 3-D point if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(413, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockInstanceInsertPoint", None, object)

    def block_instance_name(self, object):
        """        
        Returns the block name of a block instance.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an existing block insertion object.
            
        Returns
        =======

        string
        The block name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(571, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockInstanceName", None, object)

    def block_instance_xform(self, object):
        """        
        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an existing block insertion object.
            
        Returns
        =======

        array
        A transformation matrix (4x4 array of numbers) if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(415, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockInstanceXform", None, object)

    def block_instances(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def block_names(self, sort):
        """        
        Returns the names of all block definitions in the document.
    
        Parameters
        ==========

        sort, Boolean, Optional        
        Return a sorted array of block definition names.
            
        Returns
        =======

        array
        An array of block definition names if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(396, 1, (VT_VARIANT, 0), ((VT_BOOL, 1),), u"BlockNames", None, sort)

    def block_object_count(self, block):
        """        
        Returns the number of objects that make up a block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        number
        The number of objects that make up the block definition if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(416, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockObjectCount", None, block)

    def block_objects(self, block):
        """        
        Returns the identifiers of the objects that make up a block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        array
        An array of strings identifying the objects that make up a block definition if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(417, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockObjects", None, block)

    def block_path(self, block):
        """        
        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        string
        The path to the linked block file is successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(408, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"BlockPath", None, block)

    def block_u_r_l(self, block, u_r_l):
        """        
        Returns or sets the URL of a block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        u_r_l, String, Optional        
        The new URL.  If omitted, the current URL is returned.
            
        Returns
        =======

        string
        If a URL is not specified,  the current URL if successful.

        string
        If a URL is specified, the previous URL if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(402, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"BlockURL", None, block, u_r_l)

    def block_u_r_l_tag(self, block, u_r_l):
        """        
        Returns or sets the URL tag, or description, of a block definition.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        u_r_l, String, Optional        
        The new URL tag.  If omitted, the current URL tag is returned.
            
        Returns
        =======

        string
        If a URL tag is not specified,  the current URL tag if successful.

        string
        If a URL tag is specified, the previous URL tag if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(403, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"BlockURLTag", None, block, u_r_l)

    def delete_block(self, block):
        """        
        Deletes a block definition and all of it's inserted instances.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(418, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"DeleteBlock", None, block)

    def explode_block_instance(self, object):
        """        
        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an existing block definition.
            
        Returns
        =======

        array
        An array of strings identifying the newly exploded objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(419, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ExplodeBlockInstance", None, object)

    def insert_block(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_block(self, block):
        """        
        Verifies the existence of a block definition in the document.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(398, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsBlock", None, block)

    def is_block_embedded(self, block):
        """        
        Verifies that a block definition is embedded, or linked, from an external file.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(405, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsBlockEmbedded", None, block)

    def is_block_in_use(self, block, where):
        """        
        Verifies that a block definition is being used by an inserted instance.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        where, Integer, Optional        
        Where to look, where:
		0 (Default)
		Check for top level references in active document
		1
		Check for top level and nested references in active document
		2
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(406, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsBlockInUse", None, block, where)

    def is_block_instance(self, object):
        """        
        Verifies an object is a block instance.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of an existing block definition.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(420, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsBlockInstance", None, object)

    def is_block_reference(self, block):
        """        
        Verifies that a block definition is from a reference file.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(407, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsBlockReference", None, block)

    def rename_block(self, old_block, new_block):
        """        
        Renames an existing block definition.
    
        Parameters
        ==========

        old_block, String, Required        
        The name of an existing block definition.
            
        new_block, String, Required        
        The new block definition name.
            
        Returns
        =======

        string
        The new block definition name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(399, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"RenameBlock", None, old_block, new_block)

