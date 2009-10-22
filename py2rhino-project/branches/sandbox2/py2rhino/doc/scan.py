import py2rhino as p2r
from py2rhino import _base
import pythoncom

#------------------------------------------------------------------------------ 

def block_container_count(block_name):

    block_container_count_ed = True
    """
    
        Returns the number of block definitions that contain a specified block definition.

        Parameters
        ==========
        block_name  (string, Required) - The name of an existing block definition.

        Returns
        =======
        integer - The number of block definitions that contain the specified block definition if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockContainerCount

        
    """
    return _base._rsf.block_container_count(block_name)

def block_containers(block_name):

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

def block_count():

    block_count_ed = True
    """
    
        Returns the number of block definitions in the document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        Integer - The number of block definitions in the document.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockCount

        
    """
    return _base._rsf.block_count()

    
def block_names(sort=pythoncom.Empty):
    
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
    
    
def blocks(sort=pythoncom.Empty):
    
    """
    
        Returns all block definitions in the document.

        Parameters
        ==========
        sort  (boolean, Optional) - Return a sorted list of block definitions sorted according to their names.

        Returns
        =======
        list - A list of block definition names if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BlockNames

        
    """
    names = _base._rsf.block_names(sort)
    if names:
        blocks = []
        for name in names:
            block = p2r.ent.Block(name)
            blocks.append(block)
        return blocks
    else:
        return None