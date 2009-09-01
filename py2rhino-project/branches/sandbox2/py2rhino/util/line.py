# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def closest_pnt(line, point):

    """
    
        Finds the point on an infinite line that is closest to a test point.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        point  (List of float, Required) - The test point.

        Returns
        =======
        list - The point on the line that is closest to the test point is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineClosestPoint

        
    """
    return _base._rsf.line_closest_point(line, point)

def intersect_2_lines(line_1, line_2, planar=pythoncom.Empty):

    """
    
        Calculates the intersection of two non-parallel.  Note, the two lines do not have to intersect for an intersection to be found.
		The default operation of this function assumes that the two lines are co-planar.  Thus, the return value is the intersection point of the two lines.
		But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.

        Parameters
        ==========
        line_1  (List of float, Required) - Two 3-D points identifying the starting and ending points of the first line.
        line_2  (List of float, Required) - Two 3-D points identifying the starting and ending points of the second line.
        planar  (boolean, Optional) - Assume that the two lines are co-planar. The default value is True.

        Returns
        =======
        list - If planar is omitted or True, then a single 3-D intersection point if successful.
        list - If planar is False, then a list containing a point on the first line and a point on the second line if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineLineIntersection

        
    """
    return _base._rsf.line_line_intersection(line_1, line_2, planar)

def max_distance_to_pnt(line, point):

    """
    
        Finds the longest distance between the line, as a finite chord, and a point or another line.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        point  (List of float, Required) - The test point.

        Returns
        =======
        boolean - A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P).
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineMaxDistanceTo

        
    """
    return _base._rsf.line_max_distance_to(line, point)

def max_distance_to_line(line_1, line_2):

    """
    
        Finds the longest distance between the line, as a finite chord, and a point or another line.

        Parameters
        ==========
        line_1  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        line_2  (List of float, Required) - Two 3-D points identifying the starting and ending points of the test line (another finite chord).

        Returns
        =======
        boolean - A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P).
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineMaxDistanceTo

        
    """
    return _base._rsf.line_max_distance_to_2(line_1, line_2)

def min_distance_to_pnt(line, point):

    """
    
        Finds the shortest distance between the line, as a finite chord, and a point or another line.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        point  (List of float, Required) - The test point.

        Returns
        =======
        boolean - A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P).
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineMinDistanceTo

        
    """
    return _base._rsf.line_min_distance_to(line, point)

def min_distance_to_line(line_1, line_2):

    """
    
        Finds the shortest distance between the line, as a finite chord, and a point or another line.

        Parameters
        ==========
        line_1  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        line_2  (List of float, Required) - Two 3-D points identifying the starting and ending points of the test line (another finite chord).

        Returns
        =======
        boolean - A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P).
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineMinDistanceTo

        
    """
    return _base._rsf.line_min_distance_to_2(line_1, line_2)

def line_pln(line):

    """
    
        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LinePlane

        
    """
    return _base._rsf.line_plane(line)

def intersect_pln(line, plane):

    """
    
        Calculates the intersection of a line and a plane.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line to intersect.
        plane  (List of float, Required) - The plane to intersect.

        Returns
        =======
        list - The 3-D point of intersection is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LinePlaneIntersection

        
    """
    return _base._rsf.line_plane_intersection(line, plane)

def xform(line, xform):

    """
    
        Transforms a line.

        Parameters
        ==========
        line  (List of float, Required) - Two 3-D points identifying the starting and ending points of the line.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting line if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineTransform

        
    """
    return _base._rsf.line_transform(line, xform)
