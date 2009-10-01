# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_point(point):

    """
    
        Adds a point object to the document.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPoint

        
    """
    return _base._rsf.add_point(point)

def add_points(points):

    """
    
        Adds one or more point objects to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.

        Returns
        =======
        list - The identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPoints

        
    """
    return _base._rsf.add_points(points)
