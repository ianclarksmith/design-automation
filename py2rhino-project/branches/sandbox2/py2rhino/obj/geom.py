# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def bounding_box(objects, view=pythoncom.Empty, world_coords=pythoncom.Empty):

    """
    
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.

        Parameters
        ==========
        objects  (List of string, Required) - An list of strings identifying the objects.
        view  (string, Optional) - The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
        world_coords  (boolean, Optional) - Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.

        Returns
        =======
        list - A list of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BoundingBox

        
    """
    return _base._rsf.bounding_box(objects, view, world_coords)

def compare_geometry(object_1, object_2):

    """
    
        Compares two objects to determine if they are geometrically identical.

        Parameters
        ==========
        object_1  (string, Required) - The identifier of the first object to compare.
        object_2  (string, Required) - The identifier of the second object to compare.

        Returns
        =======
        boolean - True if the objects are geometrically identical, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CompareGeometry

        
    """
    return _base._rsf.compare_geometry(object_1, object_2)
