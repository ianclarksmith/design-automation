# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def block_container_count(block):

    return _rsf.block_container_count(block)

def block_containers(block):

    return _rsf.block_containers(block)

def block_count():

    return _rsf.block_count()

def block_description(block, text=pythoncom.Empty):

    return _rsf.block_description(block, text)

def block_instance_count(block):

    return _rsf.block_instance_count(block)

def block_instance_insert_point(object):

    return _rsf.block_instance_insert_point(object)

def block_instance_name(object):

    return _rsf.block_instance_name(object)

def block_instance_xform(object):

    return _rsf.block_instance_xform(object)

def block_instances(block):

    return _rsf.block_instances(block)

def block_names(sort=pythoncom.Empty):

    return _rsf.block_names(sort)

def block_object_count(block):

    return _rsf.block_object_count(block)

def block_objects(block):

    return _rsf.block_objects(block)

def block_path(block):

    return _rsf.block_path(block)

def block_u_r_l(block, u_r_l=pythoncom.Empty):

    return _rsf.block_u_r_l(block, u_r_l)

def block_u_r_l_tag(block, u_r_l=pythoncom.Empty):

    return _rsf.block_u_r_l_tag(block, u_r_l)

def delete_block(block):

    return _rsf.delete_block(block)

def explode_block_instance(object):

    return _rsf.explode_block_instance(object)

def insert_block(name, point, scale=pythoncom.Empty, angle=pythoncom.Empty, normal=pythoncom.Empty):

    return _rsf.insert_block(name, point, scale, angle, normal)

def insert_block_2(name, xform):

    return _rsf.insert_block_2(name, xform)

def is_block(block):

    return _rsf.is_block(block)

def is_block_embedded(block):

    return _rsf.is_block_embedded(block)

def is_block_in_use(block, where=pythoncom.Empty):

    return _rsf.is_block_in_use(block, where)

def is_block_instance(object):

    return _rsf.is_block_instance(object)

def is_block_reference(block):

    return _rsf.is_block_reference(block)

def rename_block(old_block, new_block):

    return _rsf.rename_block(old_block, new_block)

