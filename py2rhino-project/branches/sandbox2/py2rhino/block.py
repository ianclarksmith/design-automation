# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Block(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(411, 1, (VT_VARIANT, 0), magic, u"BlockContainerCount", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(412, 1, (VT_VARIANT, 0), magic, u"BlockContainers", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(397, 1, (VT_VARIANT, 0), magic, u"BlockCount", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [block, text]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(400, 1, (VT_VARIANT, 0), magic, u"BlockDescription", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(404, 1, (VT_VARIANT, 0), magic, u"BlockInstanceCount", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(413, 1, (VT_VARIANT, 0), magic, u"BlockInstanceInsertPoint", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(571, 1, (VT_VARIANT, 0), magic, u"BlockInstanceName", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(415, 1, (VT_VARIANT, 0), magic, u"BlockInstanceXform", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(414, 1, (VT_VARIANT, 0), magic, u"BlockInstances", None, *flattened)

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
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [sort]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(396, 1, (VT_VARIANT, 0), magic, u"BlockNames", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(416, 1, (VT_VARIANT, 0), magic, u"BlockObjectCount", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(417, 1, (VT_VARIANT, 0), magic, u"BlockObjects", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(408, 1, (VT_VARIANT, 0), magic, u"BlockPath", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [block, u_r_l]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(402, 1, (VT_VARIANT, 0), magic, u"BlockURL", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [block, u_r_l]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(403, 1, (VT_VARIANT, 0), magic, u"BlockURLTag", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(418, 1, (VT_VARIANT, 0), magic, u"DeleteBlock", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(419, 1, (VT_VARIANT, 0), magic, u"ExplodeBlockInstance", None, *flattened)

    def insert_block(self, name, point, scale=None, angle=None, normal=None):
        """        
        Inserts a block whose definition already exists in the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the block definition to insert.
            
        point, Array of Doubles, Required        
        The 3-D insertion point of the block.
            
        scale, Array of Integers, Optional        
        An array of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
            
        angle, Double, Optional        
        The rotation angle in degrees. If omitted, the block is not rotated.
            
        normal, Array of Doubles, Optional        
        A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.
            
        Returns
        =======

        string
        The identifier of the newly inserted block instance, if successful.

        null
        If not successful, or on error.

        """

        params = [name, point, scale, angle, normal]
        required = [True, True, False, False, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [name, flatten_params(point), flatten_params(scale), angle, flatten_params(normal)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(633, 1, (VT_VARIANT, 0), magic, u"InsertBlock", None, *flattened)

    def insert_block_2(self, name, xform):
        """        
        Inserts a block whose definition already exists in the document.
    
        Parameters
        ==========

        name, String, Required        
        The name of the block definition to insert.
            
        xform, Array of Doubles, Required        
        4x4 transformation matrix to apply.
            
        Returns
        =======

        string
        The identifier of the newly inserted block instance, if successful.

        null
        If not successful, or on error.

        """

        params = [name, xform]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [name, flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(633, 1, (VT_VARIANT, 0), magic, u"InsertBlock", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(398, 1, (VT_VARIANT, 0), magic, u"IsBlock", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(405, 1, (VT_VARIANT, 0), magic, u"IsBlockEmbedded", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [block, where]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(406, 1, (VT_VARIANT, 0), magic, u"IsBlockInUse", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(420, 1, (VT_VARIANT, 0), magic, u"IsBlockInstance", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(407, 1, (VT_VARIANT, 0), magic, u"IsBlockReference", None, *flattened)

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
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [old_block, new_block]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(399, 1, (VT_VARIANT, 0), magic, u"RenameBlock", None, *flattened)

