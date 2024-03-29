import pythoncom
from py2rhino import _base

def object_type(object):
    object_type_ed = True
    """
    
    Returns the type of an object.

    Parameters
    ==========
    object  (ObjectRoot, Required) - The object.

    Returns
    =======
    float - The object type if successful.  The valid object types are list in the table for type.
    None - If not successful, or on error.
    
    Table: type
    Value, Description
    0, Unknown object
    1, Point
    2, Point cloud
    4, Curve
    8, Surface or single-face brep
    16, Polysurface or multiple-face
    32, Mesh
    256, Light
    512, Annotation
    4096, Instance or block reference
    8192, Text dot object
    16384, Grip object
    32768, Detail
    65536, Hatch
    131072, Morph control
    134217728, Cage
    268435456, Phantom
    536870912, Clipping plane

    Rhinoscript
    ===========
    This function calls the Rhinoscript function: ObjectType

    
    """
    return _base._rsf.object_type(object._rhino_id)

def is_clipping_plane(object):

    """
    
    Verifies that an object is a clipping plane object.

    Parameters
    ==========
    object  (ObjectRoot, Required) - The object.

    Returns
    =======
    boolean - True if successful, otherwise False.
    None - On error.

    Rhinoscript
    ===========
    This function calls the Rhinoscript function: IsClippingPlane

        
    """
    return _base._rsf.is_clipping_plane(object._rhino_id)

def is_point(object):

    """
    
        Verifies an object is a point object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPoint

        
    """
    return _base._rsf.is_point(object)

def is_point_cloud(object):

    """
    
        Verifies an object is a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPointCloud

        
    """
    return _base._rsf.is_point_cloud(object)

def is_text(object):

    """
    
        Verifies an object is a text object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsText

        
    """
    return _base._rsf.is_text(object)

def is_text_dot(object):

    """
    
        Verifies an object is a text dot object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsTextDot

        
    """
    return _base._rsf.is_text_dot(object)


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
    
def is_block_instance(object):

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
    return _base._rsf.is_block_instance(object._rhino_id)    
