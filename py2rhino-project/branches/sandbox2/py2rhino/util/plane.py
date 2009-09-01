# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def distance_to_pln(plane, point):

    """
    
        Returns the distance from a 3-D point to a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
        point  (List of float, Required) - The 3-D point.

        Returns
        =======
        number - The distance if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DistanceToPlane

        
    """
    return _base._rsf.distance_to_plane(plane, point)

def evaluate(plane, parameter):

    """
    
        Evaluates a plane at a U,V parameter.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.

        Returns
        =======
        list - The 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EvaluatePlane

        
    """
    return _base._rsf.evaluate_plane(plane, parameter)

def intersect_3_plns(plane_1, plane_2, plane_3):

    """
    
        Calculates the intersection of three planes.

        Parameters
        ==========
        plane_1  (List of float, Required) - The first plane to intersect.
        plane_2  (List of float, Required) - The second plane to intersect.
        plane_3  (List of float, Required) - The third plane to intersect.

        Returns
        =======
        list - The 3-D point of intersection is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IntersectPlanes

        
    """
    return _base._rsf.intersect_planes(plane_1, plane_2, plane_3)

def move(plane, origin):

    """
    
        Moves the origin of a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
        origin  (List of float, Required) - A 3-D point identifying the new origin location.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MovePlane

        
    """
    return _base._rsf.move_plane(plane, origin)

def closest_pnt(plane, point, return_point=pythoncom.Empty):

    """
    
        Returns the point on a plane that is closest to a test point.

        Parameters
        ==========
        plane  (List of float, Required) - The plane. The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
        point  (List of float, Required) - The 3-D point to test.
        return_point  (boolean, Optional) - If omitted or True, then the point on the plane that is closest to the test point is returned. If False, then the parameter of the point on the plane that is closest to the test point is returned.

        Returns
        =======
        list - If return_point is omitted or True, then the 3-D point if successful. If return_point is False, then a list containing the U,V parameters of the point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneClosestPoint

        
    """
    return _base._rsf.plane_closest_point(plane, point, return_point)

def equation(plane):

    """
    
        Returns the equation of  a plane. The standard equation of a plane with a non-zero normal vector is as follows:
		Ax + By + Cz + D = 0

        Parameters
        ==========
        plane  (List of float, Required) - The plane. The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3

        Returns
        =======
        list - A list containing four numbers that represent the coefficients of the equation, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneEquation

        
    """
    return _base._rsf.plane_equation(plane)

def fit_from_pnts(points):

    """
    
        Returns a plane that was fit through an array of 3-D points.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneFitFromPoints

        
    """
    return _base._rsf.plane_fit_from_points(points)

def from_frame(origin, xaxis, yaxis):

    """
    
        Construct a plane from a point, and two vectors in the plane.

        Parameters
        ==========
        origin  (List of float, Required) - A 3-D point identifying the origin of the plane.
        xaxis  (List of float, Required) - A non-zero 3-D vector in the plane that determines the X axis direction.
        yaxis  (List of float, Required) - A non-zero 3-D vector not parallel to arrXaxis that is used to determine the Y axis direction. Note, arrYaxis does not have to be perpendicular to arrXaxis.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneFromFrame

        
    """
    return _base._rsf.plane_from_frame(origin, xaxis, yaxis)

def from_normal(origin, normal):

    """
    
        Creates a plane from an origin point and a normal direction vector.

        Parameters
        ==========
        origin  (List of float, Required) - A 3-D point identifying the origin of the plane.
        normal  (List of float, Required) - A non-zero 3-D vector identifying the normal direction of the plane.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneFromNormal

        
    """
    return _base._rsf.plane_from_normal(origin, normal)

def from_pnts(origin, point_x, point_y):

    """
    
        Creates a plane from three non-colinear points.

        Parameters
        ==========
        origin  (List of float, Required) - The first point, or origin, of the plane.
        point_x  (List of float, Required) - A point on the plane's X axis.
        point_y  (List of float, Required) - A point on the plane's Y axis.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneFromPoints

        
    """
    return _base._rsf.plane_from_points(origin, point_x, point_y)

def intersect_2_plns(plane_1, point_2):

    """
    
        Calculates the intersection of two planes.

        Parameters
        ==========
        plane_1  (List of float, Required) - The first plane to intersect.
        point_2  (List of float, Required) - The second plane to intersect.

        Returns
        =======
        list - Two 3-D points identifying the starting and ending points of the intersection line.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlanePlaneIntersection

        
    """
    return _base._rsf.plane_plane_intersection(plane_1, point_2)

def xform(plane, xform):

    """
    
        Transforms a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane to transform.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting plane if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneTransform

        
    """
    return _base._rsf.plane_transform(plane, xform)

def rotate(plane, angle, axis):

    """
    
        Rotates a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
        angle  (float, Required) - The rotation angle in degrees.
        axis  (List of float, Required) - A non-zero 3-D vector identifying the axis of rotation.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RotatePlane

        
    """
    return _base._rsf.rotate_plane(plane, angle, axis)

def world_x_y_plane():

    """
    
        Returns Rhino's world XY plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(1.0,0.0,0.0), Array(0.0,1.0,0.0)

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - Rhino's world XY plane.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: WorldXYPlane

        
    """
    return _base._rsf.world_x_y_plane()

def world_y_z_plane():

    """
    
        Returns Rhino's world YZ plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,1.0,0.0), Array(0.0,0.0,1.0)

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - Rhino's world YZ plane.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: WorldYZPlane

        
    """
    return _base._rsf.world_y_z_plane()

def world_z_x_plane():

    """
    
        Returns Rhino's world ZX plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,0.0,1.0), Array(1.0,0.0,0.0)

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - Rhino's world ZX plane.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: WorldZXPlane

        
    """
    return _base._rsf.world_z_x_plane()
