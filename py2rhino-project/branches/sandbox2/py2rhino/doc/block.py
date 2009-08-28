# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def container_count(block_name):

    """
    For help, look up the Rhinoscript function: BlockContainerCount
    """
    return base._rsf.block_container_count(block_name)

def containers(block_name):

    """
    For help, look up the Rhinoscript function: BlockContainers
    """
    return base._rsf.block_containers(block_name)

def count():

    """
    For help, look up the Rhinoscript function: BlockCount
    """
    return base._rsf.block_count()

def description(block_name, text=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: BlockDescription
    """
    return base._rsf.block_description(block_name, text)

def instance_count(block_name):

    """
    For help, look up the Rhinoscript function: BlockInstanceCount
    """
    return base._rsf.block_instance_count(block_name)

def instance_insert_point(block_id):

    """
    For help, look up the Rhinoscript function: BlockInstanceInsertPoint
    """
    return base._rsf.block_instance_insert_point(block_id)

def instance_name(block_id):

    """
    For help, look up the Rhinoscript function: BlockInstanceName
    """
    return base._rsf.block_instance_name(block_id)

def instance_xform(block_id):

    """
    For help, look up the Rhinoscript function: BlockInstanceXform
    """
    return base._rsf.block_instance_xform(block_id)

def instances(block_name):

    """
    For help, look up the Rhinoscript function: BlockInstances
    """
    return base._rsf.block_instances(block_name)

def names(sort=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: BlockNames
    """
    return base._rsf.block_names(sort)

def object_count(block_name):

    """
    For help, look up the Rhinoscript function: BlockObjectCount
    """
    return base._rsf.block_object_count(block_name)

def objects(block_name):

    """
    For help, look up the Rhinoscript function: BlockObjects
    """
    return base._rsf.block_objects(block_name)

def path(block_name):

    """
    For help, look up the Rhinoscript function: BlockPath
    """
    return base._rsf.block_path(block_name)

def url(block_name, url=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: BlockURL
    """
    return base._rsf.block_u_r_l(block_name, url)

def url_tag(block_name, url=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: BlockURLTag
    """
    return base._rsf.block_u_r_l_tag(block_name, url)

def delete(block_name):

    """
    For help, look up the Rhinoscript function: DeleteBlock
    """
    return base._rsf.delete_block(block_name)

def explode_instance(block_id):

    """
    For help, look up the Rhinoscript function: ExplodeBlockInstance
    """
    return base._rsf.explode_block_instance(block_id)

def insert(block_name, insertion_point, scale=pythoncom.Empty, angle=pythoncom.Empty, normal=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: InsertBlock
    """
    return base._rsf.insert_block(block_name, insertion_point, scale, angle, normal)

def insert_by_xform(block_name, xform):

    """
    For help, look up the Rhinoscript function: InsertBlock2
    """
    return base._rsf.insert_block_2(block_name, xform)

def is_block(block_name):

    """
    For help, look up the Rhinoscript function: IsBlock
    """
    return base._rsf.is_block(block_name)

def is_embedded(block_name):

    """
    For help, look up the Rhinoscript function: IsBlockEmbedded
    """
    return base._rsf.is_block_embedded(block_name)

def is_in_use(block_name, where=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: IsBlockInUse
    """
    return base._rsf.is_block_in_use(block_name, where)

def is_instance(block_id):

    """
    For help, look up the Rhinoscript function: IsBlockInstance
    """
    return base._rsf.is_block_instance(block_id)

def is_reference(block_name):

    """
    For help, look up the Rhinoscript function: IsBlockReference
    """
    return base._rsf.is_block_reference(block_name)

def rename(old_block_name, new_block_name):

    """
    For help, look up the Rhinoscript function: RenameBlock
    """
    return base._rsf.rename_block(old_block_name, new_block_name)
