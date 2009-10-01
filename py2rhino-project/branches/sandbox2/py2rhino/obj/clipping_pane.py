# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_clipping_plane(plane, d_u, d_v, views=pythoncom.Empty):

    """
    
        Creates a clipping plane. A clipping plane is a plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.
        d_u  (float, Required) - The magnitude in the U direction.
        d_v  (float, Required) - The magnitude in the V direction.
        views  (List of string, Optional) - The titles of the views to clip.  If omitted, the current active view is used.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddClippingPlane

        
    """
    return _base._rsf.add_clipping_plane(plane, d_u, d_v, views)
