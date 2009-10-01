# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def is_clipping_plane(object):

    """
    
        Verifies that an object is a clipping plane object.

        Parameters
        ==========
        object  (string, Required) - The object's identifier.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsClippingPlane

        
    """
    return _base._rsf.is_clipping_plane(object)

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
