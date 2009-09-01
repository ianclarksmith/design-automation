# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add(point_1, point_2):

    """
    
        Adds a 3-D point or a 3-D vector to a 3-D point.

        Parameters
        ==========
        point_1  (List of float, Required) - The 3-D point to add to.
        point_2  (List of float, Required) - The 3-D point or a 3-D vector to add.

        Returns
        =======
        list - The resulting 3-D point if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointAdd

        
    """
    return _base._rsf.point_add(point_1, point_2)

def points_bounding_box(points, view=pythoncom.Empty, world_coords=pythoncom.Empty):

    """
    
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.
        view  (string, Optional) - The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
        world_coords  (boolean, Optional) - Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.

        Returns
        =======
        list - A list of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointArrayBoundingBox

        
    """
    return _base._rsf.point_array_bounding_box(points, view, world_coords)

def points_closest_point(points, point):

    """
    
        Finds the point in an array of 3-D points that is closest to a test point.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points to test.
        point  (List of float, Required) - The 3-D test point.

        Returns
        =======
        number - The index of the element in the point list that is closest to the test point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointArrayClosestPoint

        
    """
    return _base._rsf.point_array_closest_point(points, point)

def points_transform(points, xform):

    """
    
        Transforms an array of 3-D points.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points to transform.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting list of 3-D points if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointArrayTransform

        
    """
    return _base._rsf.point_array_transform(points, xform)

def compare(point_1, point_2, tolerance=pythoncom.Empty):

    """
    
        Compares two 3-D points.

        Parameters
        ==========
        point_1  (List of float, Required) - The first 3-D point to compare.
        point_2  (List of float, Required) - The second 3-D point to compare.
        tolerance  (float, Optional) - The tolerance to use for the comparison. If omitted, Rhino's internal zero tolerance is used.

        Returns
        =======
        boolean - True or False
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointCompare

        
    """
    return _base._rsf.point_compare(point_1, point_2, tolerance)

def divide(point, scale):

    """
    
        Divides a 3-D point by a value

        Parameters
        ==========
        point  (List of float, Required) - The 3-D point to divide.
        scale  (float, Required) - The a non-zero value to divide.

        Returns
        =======
        list - The resulting 3-D point if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointDivide

        
    """
    return _base._rsf.point_divide(point, scale)

def scale(point, scale):

    """
    
        Scales a 3-D point.

        Parameters
        ==========
        point  (List of float, Required) - The 3-D point to scale.
        scale  (float, Required) - The scale factor to apply.

        Returns
        =======
        list - The resulting 3-D point if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointScale

        
    """
    return _base._rsf.point_scale(point, scale)

def subtract(point_1, point_2):

    """
    
        Subtracts a 3-D point or a 3-D vector from a 3-D point.

        Parameters
        ==========
        point_1  (List of float, Required) - The 3-D point to subtract from.
        point_2  (List of float, Required) - The 3-D point or a 3-D vector to subtract.

        Returns
        =======
        list - The resulting 3-D point if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointSubtract

        
    """
    return _base._rsf.point_subtract(point_1, point_2)

def transform(point, xform):

    """
    
        Transforms a 3-D point.

        Parameters
        ==========
        point  (List of float, Required) - The 3-D point to transform.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting 3-D point if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointTransform

        
    """
    return _base._rsf.point_transform(point, xform)

def points_are_coplanar(points, tolerance=pythoncom.Empty):

    """
    
        Verifies that an array of 3-D points are co-planar.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.
        tolerance  (float, Optional) - A tolerance to use when verifying. The default is to use Rhino's internal zero tolerance (1.0e-12).

        Returns
        =======
        boolean - True or False indicating either coplanar or not coplanar, respectively, if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointsAreCoplanar

        
    """
    return _base._rsf.points_are_coplanar(points, tolerance)

def project_point_to_mesh(points, meshes, direction):

    """
    
        Projects one or more points onto one or more meshes.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points to project.
        meshes  (list of mesh object, Required) - The identifiers of the mesh objects to project onto.
        direction  (List of float, Required) - The direction (3-D vector) to project the points.

        Returns
        =======
        list - A list of 3-D points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ProjectPointToMesh

        
    """
    if type(meshes) != list and type(meshes) != tuple:
        meshes = (meshes,)
    return _base._rsf.project_point_to_mesh(points, map(lambda i: i._rhino_id, meshes), direction)

def project_point_to_surface(points, surfaces, direction):

    """
    
        Projects one or more points onto one or more surfaces or polysurfaces.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points to project.
        surfaces  (list of SurfaceRoot, Required) - The identifiers of the surface or polysurface objects to project onto.
        direction  (List of float, Required) - The direction (3-D vector) to project the points.

        Returns
        =======
        list - A list of 3-D points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ProjectPointToSurface

        
    """
    if type(surfaces) != list and type(surfaces) != tuple:
        surfaces = (surfaces,)
    return _base._rsf.project_point_to_surface(points, map(lambda i: i._rhino_id, surfaces), direction)

def pull_points(object, points):

    """
    
        Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.

        Parameters
        ==========
        object  (object, Required) - The identifier of the surface or mesh object that pulls.
        points  (List of float, Required) - An list of 3-D points to pull.

        Returns
        =======
        list - A list of 3-D points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PullPoints

        
    """
    return _base._rsf.pull_points(object._rhino_id, points)
