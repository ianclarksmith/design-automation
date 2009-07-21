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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(411, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockContainerCount", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(412, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockContainers", None, *params_flattened)

    def block_count():
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

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(397, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockCount", None, *params_flattened)

    def block_description(self, block, text=None):
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

        params = [block, text]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [block, text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(400, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockDescription", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(404, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockInstanceCount", None, *params_flattened)

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

        return self._ApplyTypes_(413, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockInstanceInsertPoint", None, *params_flattened)

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

        return self._ApplyTypes_(571, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockInstanceName", None, *params_flattened)

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

        return self._ApplyTypes_(415, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockInstanceXform", None, *params_flattened)

    def block_instances(self, block):
        """        
        Returns the identifiers of the inserted instances of a block.
    
        Parameters
        ==========

        block, String, Required        
        The name of an existing block definition.
            
        Returns
        =======

        array
        An array of strings identifying the instances of a block if successful.

        null
        If not successful, or on error.

        """

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(414, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockInstances", None, *params_flattened)

    def block_names(self, sort=None):
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

        params = [sort]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [sort]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(396, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockNames", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(416, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockObjectCount", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(417, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockObjects", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(408, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockPath", None, *params_flattened)

    def block_u_r_l(self, block, u_r_l=None):
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

        params = [block, u_r_l]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [block, u_r_l]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(402, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockURL", None, *params_flattened)

    def block_u_r_l_tag(self, block, u_r_l=None):
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

        params = [block, u_r_l]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [block, u_r_l]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(403, 1, (VT_VARIANT, 0), params_magic_numbers, u"BlockURLTag", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(418, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteBlock", None, *params_flattened)

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

        return self._ApplyTypes_(419, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExplodeBlockInstance", None, *params_flattened)

    def insert_block(self, name, point, scale=None, angle=None, normal=None, xform):
        """        
        Inserts a block whose definition already exists in the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the block definition to insert.
            
        point, Array of ????, Required        
        The 3-D insertion point of the block.
            
        scale, Array of ????, Optional        
        An array of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
            
        angle, Double, Optional        
        The rotation angle in degrees. If omitted, the block is not rotated.
            
        normal, Array of ????, Optional        
        A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.
            
        xform, Array of ????, Required        
        4x4 transformation matrix to apply.
            
        Returns
        =======

        string
        The identifier of the newly inserted block instance, if successful.

        null
        If not successful, or on error.

        """

        params = [name, point, scale, angle, normal, xform]
        params_required = [True, True, False, False, False, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [name, flatten(point), flatten(scale), angle, flatten(normal), flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(633, 1, (VT_VARIANT, 0), params_magic_numbers, u"InsertBlock", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(398, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBlock", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(405, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBlockEmbedded", None, *params_flattened)

    def is_block_in_use(self, block, where=None):
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

        params = [block, where]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [block, where]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(406, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBlockInUse", None, *params_flattened)

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

        return self._ApplyTypes_(420, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBlockInstance", None, *params_flattened)

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

        params = [block]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(407, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBlockReference", None, *params_flattened)

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

        params = [old_block, new_block]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [old_block, new_block]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(399, 1, (VT_VARIANT, 0), params_magic_numbers, u"RenameBlock", None, *params_flattened)

