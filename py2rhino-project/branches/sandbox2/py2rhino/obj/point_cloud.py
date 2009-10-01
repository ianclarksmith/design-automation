# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_point_cloud(points):

    """
    
        Adds a point cloud object to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPointCloud

        
    """
    return _base._rsf.add_point_cloud(points)

def point_cloud_count(object):

    """
    
        Returns the point count of a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The identifier of a point cloud object.

        Returns
        =======
        number - The number of points if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointCloudCount

        
    """
    return _base._rsf.point_cloud_count(object)

def point_cloud_points(object):

    """
    
        Returns the points of a point cloud object.

        Parameters
        ==========
        object  (string, Required) - The identifier of a point cloud object.

        Returns
        =======
        list - A list of 3-D points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointCloudPoints

        
    """
    return _base._rsf.point_cloud_points(object)
