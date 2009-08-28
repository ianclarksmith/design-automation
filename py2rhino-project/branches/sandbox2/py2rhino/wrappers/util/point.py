# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.wrappers import base

def add(point_1, point_2):

    """
    For help, look up the Rhinoscript function: PointAdd
    """
    return base._rsf.point_add(point_1, point_2)

def points_bounding_box(points, view=pythoncom.Empty, world_coords=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: PointArrayBoundingBox
    """
    return base._rsf.point_array_bounding_box(points, view, world_coords)

def points_closest_point(points, point):

    """
    For help, look up the Rhinoscript function: PointArrayClosestPoint
    """
    return base._rsf.point_array_closest_point(points, point)

def points_transform(points, xform):

    """
    For help, look up the Rhinoscript function: PointArrayTransform
    """
    return base._rsf.point_array_transform(points, xform)

def compare(point_1, point_2, tolerance=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: PointCompare
    """
    return base._rsf.point_compare(point_1, point_2, tolerance)

def divide(point, scale):

    """
    For help, look up the Rhinoscript function: PointDivide
    """
    return base._rsf.point_divide(point, scale)

def scale(point, scale):

    """
    For help, look up the Rhinoscript function: PointScale
    """
    return base._rsf.point_scale(point, scale)

def subtract(point_1, point_2):

    """
    For help, look up the Rhinoscript function: PointSubtract
    """
    return base._rsf.point_subtract(point_1, point_2)

def transform(point, xform):

    """
    For help, look up the Rhinoscript function: PointTransform
    """
    return base._rsf.point_transform(point, xform)

def points_are_coplanar(points, tolerance=pythoncom.Empty):

    """
    For help, look up the Rhinoscript function: PointsAreCoplanar
    """
    return base._rsf.points_are_coplanar(points, tolerance)

def project_point_to_mesh(points, meshes, direction):

    """
    For help, look up the Rhinoscript function: ProjectPointToMesh
    """
    if type(meshes) != list and type(meshes) != tuple:
        meshes = (meshes,)
    return base._rsf.project_point_to_mesh(points, map(lambda i: i._rhino_id, meshes), direction)

def project_point_to_surface(points, surfaces, direction):

    """
    For help, look up the Rhinoscript function: ProjectPointToSurface
    """
    if type(surfaces) != list and type(surfaces) != tuple:
        surfaces = (surfaces,)
    return base._rsf.project_point_to_surface(points, map(lambda i: i._rhino_id, surfaces), direction)

def pull_points(object, points):

    """
    For help, look up the Rhinoscript function: PullPoints
    """
    return base._rsf.pull_points(object._rhino_id, points)
