# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def container_count(block_name):

    """
    
        Returns the number of block definitions that contain a specified block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        number - The number of block definitions that contain the specified block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockContainerCount

        
    """
    return _base._rsf.block_container_count(block_name)

def containers(block_name):

    """
    
        Returns the names of the block definitions that contain a specified block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        list - A list of block definition names if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockContainers

        
    """
    return _base._rsf.block_containers(block_name)

def count():

    """
    
        Returns the number of block definitions in the document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of block definitions in the document.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockCount

        
    """
    return _base._rsf.block_count()

def description(block_name, text=pythoncom.Empty):

    """
    
        Returns or sets the description of a block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.
        text  (string, Optional) - The new description.  If omitted, the current description is returned.

        Returns
        =======
        string - If a description is not specified,  the current description if successful.
        string - If a description is specified, the previous description if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockDescription

        
    """
    return _base._rsf.block_description(block_name, text)

def instance_count(block_name):

    """
    
        Counts the number of instances of the block in the document.  Nested instances are not included in the count.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        number - The number of instances of the block in the document if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceCount

        
    """
    return _base._rsf.block_instance_count(block_name)

def instance_insert_point(block_id):

    """
    
        Returns the insertion point of a block instance.

        Parameters
        ==========
        block_id  (string, Required) - The identifier of an existing block insertion object.

        Returns
        =======
        list - A 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceInsertPoint

        
    """
    return _base._rsf.block_instance_insert_point(block_id)

def instance_name(block_id):

    """
    
        Returns the block name of a block instance.

        Parameters
        ==========
        block_id  (string, Required) - The identifier of an existing block insertion object.

        Returns
        =======
        string - The block name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceName

        
    """
    return _base._rsf.block_instance_name(block_id)

def instance_xform(block_id):

    """
    
        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix

        Parameters
        ==========
        block_id  (string, Required) - The identifier of an existing block insertion object.

        Returns
        =======
        list - A transformation matrix (4x4 list of numbers) if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstanceXform

        
    """
    return _base._rsf.block_instance_xform(block_id)

def instances(block_name):

    """
    
        Returns the identifiers of the inserted instances of a block.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        list - A list of strings identifying the instances of a block if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockInstances

        
    """
    return _base._rsf.block_instances(block_name)

def names(sort=pythoncom.Empty):

    """
    
        Returns the names of all block definitions in the document.

        Parameters
        ==========
        sort  (boolean, Optional) - Return a sorted list of block definition names.

        Returns
        =======
        list - A list of block definition names if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockNames

        
    """
    return _base._rsf.block_names(sort)

def object_count(block_name):

    """
    
        Returns the number of objects that make up a block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        number - The number of objects that make up the block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockObjectCount

        
    """
    return _base._rsf.block_object_count(block_name)

def objects(block_name):

    """
    
        Returns the identifiers of the objects that make up a block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        list - A list of strings identifying the objects that make up a block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockObjects

        
    """
    return _base._rsf.block_objects(block_name)

def path(block_name):

    """
    
        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        string - The path to the linked block file is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockPath

        
    """
    return _base._rsf.block_path(block_name)

def url(block_name, url=pythoncom.Empty):

    """
    
        Returns or sets the URL of a block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.
        url  (string, Optional) - The new URL.  If omitted, the current URL is returned.

        Returns
        =======
        string - If a URL is not specified,  the current URL if successful.
        string - If a URL is specified, the previous URL if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockURL

        
    """
    return _base._rsf.block_u_r_l(block_name, url)

def url_tag(block_name, url=pythoncom.Empty):

    """
    
        Returns or sets the URL tag, or description, of a block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.
        url  (string, Optional) - The new URL tag.  If omitted, the current URL tag is returned.

        Returns
        =======
        string - If a URL tag is not specified,  the current URL tag if successful.
        string - If a URL tag is specified, the previous URL tag if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockURLTag

        
    """
    return _base._rsf.block_u_r_l_tag(block_name, url)

def delete(block_name):

    """
    
        Deletes a block definition and all of it's inserted instances.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteBlock

        
    """
    return _base._rsf.delete_block(block_name)

def explode_instance(block_id):

    """
    
        Explodes a block instance into it's geometric components.  The exploded objects are added to the document.

        Parameters
        ==========
        block_id  (string, Required) - The identifier of an existing block definition.

        Returns
        =======
        list - A list of strings identifying the newly exploded objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExplodeBlockInstance

        
    """
    return _base._rsf.explode_block_instance(block_id)

def insert(block_name, insertion_point, scale=pythoncom.Empty, angle=pythoncom.Empty, normal=pythoncom.Empty):

    """
    
        Inserts a block whose definition already exists in the document.

        Parameters
        ==========
        block_name  (string, Required) - The name of the block definition to insert.
        insertion_point  (List of float, Required) - The 3-D insertion point of the block.
        scale  (List of float, Optional) - An list of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
        angle  (float, Optional) - The rotation angle in degrees. If omitted, the block is not rotated.
        normal  (List of float, Optional) - A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.

        Returns
        =======
        string - The newly inserted block instance, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertBlock

        
    """
    return _base._rsf.insert_block(block_name, insertion_point, scale, angle, normal)

def insert_by_xform(block_name, xform):

    """
    
        Inserts a block whose definition already exists in the document.

        Parameters
        ==========
        block_name  (string, Required) - The name of the block definition to insert.
        xform  (List of float, Required) - 4x4 transformation matrix to apply.

        Returns
        =======
        string - The newly inserted block instance, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertBlock

        
    """
    return _base._rsf.insert_block_2(block_name, xform)

def is_block(block_name):

    """
    
        Verifies the existence of a block definition in the document.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlock

        
    """
    return _base._rsf.is_block(block_name)

def is_embedded(block_name):

    """
    
        Verifies that a block definition is embedded, or linked, from an external file.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockEmbedded

        
    """
    return _base._rsf.is_block_embedded(block_name)

def is_in_use(block_name, where=pythoncom.Empty):

    """
    
        Verifies that a block definition is being used by an inserted instance.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.
        where  (integer, Optional) - Where to look, where:
		0 (Default)
		Check for top level references in active document
		1
		Check for top level and nested references in active document
		2

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockInUse

        
    """
    return _base._rsf.is_block_in_use(block_name, where)

def is_instance(block_id):

    """
    
        Verifies an object is a block instance.

        Parameters
        ==========
        block_id  (string, Required) - The identifier of an existing block definition.

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockInstance

        
    """
    return _base._rsf.is_block_instance(block_id)

def is_reference(block_name):

    """
    
        Verifies that a block definition is from a reference file.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBlockReference

        
    """
    return _base._rsf.is_block_reference(block_name)

def rename(old_block_name, new_block_name):

    """
    
        Renames an existing block definition.

        Parameters
        ==========
        old_block_name  (string, Required) - The name of an existing block definition.
        new_block_name  (string, Required) - The new block definition name.

        Returns
        =======
        string - The new block definition name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RenameBlock

        
    """
    return _base._rsf.rename_block(old_block_name, new_block_name)
