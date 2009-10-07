

class line():

        closest_pnt = """
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
        intersect_2_lines = """
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
        max_distance_to_pnt = """
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
        max_distance_to_line = """
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
        min_distance_to_pnt = """
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
        min_distance_to_line = """
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
        line_pln = """
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
        intersect_pln = """
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
        xform = """
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


class plane():

        distance_to_pln_ed = True
        distance_to_pln = """
        Returns the distance from a 3-D point to a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are in the table for plane.
        point  (List of float, Required) - The 3-D point.
        
        Table: plane
		Element, Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 

        Returns
        =======
        float - The distance if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DistanceToPlane

        """
        evaluate_ed = True;
        evaluate = """
        Evaluates a plane at a U,V parameter.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are in the table for plane.
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.
		
		Table: plane
		Element, Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 

        Returns
        =======
        list - The 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EvaluatePlane

        """
        intersect_3_plns = """
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
        move_ed = True
        move = """
        Moves the origin of a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are listed in the table for plane.
        origin  (List of float, Required) - A 3-D point identifying the new origin location.
		
		Table: plane
		Element, Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 


        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MovePlane

        """
        closest_pnt_ed = True
        closest_pnt = """
        Returns the point on a plane that is closest to a test point.

        Parameters
        ==========
        plane  (List of float, Required) - The plane. The elements of a plane list are listed in the table for plane.
        point  (List of float, Required) - The 3-D point to test.
        return_point  (boolean, Optional) - If omitted or True, then the point on the plane that is closest to the test point is returned. If False, then the parameter of the point on the plane that is closest to the test point is returned.
        		
		Table: plane
		Element, Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 

        Returns
        =======
        list - If return_point is omitted or True, then the 3-D point if successful. If return_point is False, then a list containing the U,V parameters of the point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneClosestPoint

        """
        equation_ed = True
        equation = """
        Returns the equation of  a plane. The standard equation of a plane with a non-zero normal vector is as follows:
		Ax + By + Cz + D = 0

        Parameters
        ==========
        plane  (List of float, Required) - The plane. The elements of a plane are listed in the table for plane.
		
		Table: plane
		Element,Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 

        Returns
        =======
        list - A list containing four numbers that represent the coefficients of the equation, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneEquation

        """
        fit_from_pnts = """
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
        from_frame_ed = True
        from_frame = """
        Construct a plane from a point, and two vectors in the plane.

        Parameters
        ==========
        origin  (List of float, Required) - A 3-D point identifying the origin of the plane.
        xaxis  (List of float, Required) - A non-zero 3-D vector in the plane that determines the X axis direction.
        yaxis  (List of float, Required) - A non-zero 3-D vector not parallel to xaxis that is used to determine the Y axis direction. Note, yaxis does not have to be perpendicular to xaxis.

        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlaneFromFrame

        """
        from_normal = """
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
        from_pnts = """
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
        intersect_2_plns = """
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
        xform = """
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
        rotate = True
        rotate = """
        Rotates a plane.

        Parameters
        ==========
        plane  (List of float, Required) - The plane.  The elements of a plane list are listed in the table for plane.
        angle  (float, Required) - The rotation angle in degrees.
        axis  (List of float, Required) - A non-zero 3-D vector identifying the axis of rotation.

        Table: plane
		Element, Description
		0, Required.  The plane's origin (3-D point).
		1, Required.  The plane's X axis direction (3-D vector).
		2, Required.  The plane's Y axis direction (3-D vector).
		3, Optional.  The plane's Z axis direction (3-D vector). 
		
        Returns
        =======
        list - The plane if successful.  The elements of a plane list are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RotatePlane

        """
        world_x_y_plane = """
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
        world_y_z_plane = """
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
        world_z_x_plane = """
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


class point():

        add = """
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
        points_bounding_box = """
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
        points_closest_point_ed = True
        points_closest_point = """
        Finds the point in an array of 3-D points that is closest to a test point.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points to test.
        point  (List of float, Required) - The 3-D test point.

        Returns
        =======
        float - The index of the element in the point list that is closest to the test point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointArrayClosestPoint

        """
        points_transform = """
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
        compare = """
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
        divide = """
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
        scale = """
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
        subtract = """
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
        transform = """
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
        points_are_coplanar = """
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
        project_point_to_mesh = """
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
        project_point_to_surface = """
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
        pull_points = """
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


class vector():

        is_parallel_to = """
        Compares two vectors to see if they are parallel.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector.
        vector_2  (List of float, Required) - The 3-D vector to compare to.

        Returns
        =======
        number - The result of the comparison if successful. The possible results are as follows:
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorParallelTo

        """
        is_perpendicular_to = """
        Compares two vectors to see if they are perpendicular.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector.
        vector_2  (List of float, Required) - The 3-D vector to compare to.

        Returns
        =======
        boolean - True if the vectors are perpendicular, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorPerpendicularTo

        """
        is_tiny = """
        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to test.

        Returns
        =======
        boolean - True if the vector is tiny, otherwise False, if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorTiny

        """
        is_zero = """
        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to test.

        Returns
        =======
        boolean - True if the vector is zero, otherwise False, if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorZero

        """
        add = """
        Adds two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector to add to.
        vector_2  (List of float, Required) - The 3-D vector to add.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorAdd

        """
        compare = """
        Compares two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector to compare.
        vector_2  (List of float, Required) - The second 3-D vector to compare.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCompare

        """
        create = """
        Creates a vector from two 3-D points.

        Parameters
        ==========
        point_1  (List of float, Required) - The first 3-D point.
        point_2  (List of float, Required) - The second 3-D point.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCreate

        """
        cross_product = """
        Calculates the cross product of two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCrossProduct

        """
        divide = """
        Divides a 3-D vectors by a value

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to divide.
        divide  (float, Required) - The a non-zero value to divide.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorDivide

        """
        dot_product = """
        Calculates the dot product of two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorDotProduct

        """
        length = """
        Returns the length of a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorLength

        """
        
        multiply_ed = True
        multiply = """
        Multiplies two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        float - The resulting inner (dot) product if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorMultiply

        """
        reverse = """
        Reverses the direction of a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorReverse

        """
        rotate = """
        Rotates a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.
        angle  (float, Required) - The rotation angle in degrees.
        axis  (List of float, Required) - A 3-D vector defining the axis of rotation.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorRotate

        """
        scale = """
        Scales a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to scale.
        scale  (float, Required) - The scale factor to apply.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorScale

        """
        subtract = """
        Subtracts two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector to subtract from.
        vector_2  (List of float, Required) - The 3-D vector to subtract.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorSubtract

        """
        transform = """
        Transforms a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to transform.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorTransform

        """
        unitize = """
        Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to unitize.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorUnitize

        """
