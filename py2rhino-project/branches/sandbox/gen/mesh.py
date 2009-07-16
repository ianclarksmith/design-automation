# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Mesh(IRhinoScript):



    def add_mesh(self, vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors):
        """

        Adds a mesh object to the document.

        Parameters

        Vertices : Required, Array, arrdbl, Array of ?
        FaceVertices : Required, Array, arrdbl, Array of ?
        VertexNormals : Optional, Array, arrdbl, Array of ?
        TextureCoordinates : Optional, Array, arrdbl, Array of ?
        VertexColors : Optional, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(494, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0), (8197, 0), (8197, 0),), u'AddMesh', None, _utils.flatten(vertices), _utils.flatten(face_vertices), _utils.flatten(vertex_normals), _utils.flatten(texture_coordinates), _utils.flatten(vertex_colors))

    def add_planar_mesh(self, object, delete):
        """

        Creates a planar mesh from a closed, planar curve.

        Parameters

        Object : Required, String, str, String
        Delete : Required, Boolean, bln, Boolean

        Returns

        String : An string identifying the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(915, 1, (12, 0), ((8, 0), (11, 0),), u'AddPlanarMesh', None, object, delete)

    def curve_mesh_intersection(self, curve, mesh, return_faces):
        """

        Calculates the intersection of a curve object and a mesh object.

        Parameters

        Curve : Required, String, str, String
        Mesh : Required, String, str, String
        ReturnFaces : Optional, Boolean, bln, Boolean

        Returns

        Array : If blnReturnFaces is either omitted or False, then an array intersection points, if successful.
        Array : If blnReturnFaces is True, then a one-dimensional array containing information about each intersection if successful.  Each array element is a one-dimensional array that contains the following two elements:
        Array : The 3-D intersection point.
        Number : The mesh face index on which the intersection point lies.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(842, 1, (12, 0), ((8, 0), (8, 0), (11, 0),), u'CurveMeshIntersection', None, curve, mesh, return_faces)

    def disjoint_mesh_count(self, object):
        """

        Returns the number of meshes that could be created by calling SplitDisjointMesh.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of meshes that could be created if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(721, 1, (12, 0), ((8, 0),), u'DisjointMeshCount', None, object)

    def duplicate_mesh_border(self, object):
        """

        Creates a curve that duplicates a mesh border.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of strings identifying the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(853, 1, (12, 0), ((8, 0),), u'DuplicateMeshBorder', None, object)

    def explode_meshes(self, object, objects, delete):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_mesh(self, object):
        """

        Verifies an object is a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(119, 1, (12, 0), ((8, 0),), u'IsMesh', None, object)

    def is_mesh_closed(self, object):
        """

        Verifies a mesh object is closed.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(355, 1, (12, 0), ((8, 0),), u'IsMeshClosed', None, object)

    def is_mesh_manifold(self, object):
        """

        Verifies a mesh object is manifold.  A mesh for which every edge is shared by at most two faces is called a manifold.  If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(855, 1, (12, 0), ((8, 0),), u'IsMeshManifold', None, object)

    def mesh_area(self, object, objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def mesh_area_centroid(self, object):
        """

        Calculates the area centroid of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : A 3-D point identifying the area centroid if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(477, 1, (12, 0), ((8, 0),), u'MeshAreaCentroid', None, object)

    def mesh_boolean_difference(self, input0, input1, delete):
        """

        Performs a Boolean difference operation on two sets of input meshes. For more details, see the MeshBooleanDifference command in the Rhino help file.

        Parameters

        Input0 : Required, Array, arrdbl, Array of ?
        Input1 : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(732, 1, (12, 0), ((8197, 0), (8197, 0), (11, 0),), u'MeshBooleanDifference', None, _utils.flatten(input0), _utils.flatten(input1), delete)

    def mesh_boolean_intersection(self, input0, input1, delete):
        """

        Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.

        Parameters

        Input0 : Required, Array, arrdbl, Array of ?
        Input1 : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(733, 1, (12, 0), ((8197, 0), (8197, 0), (11, 0),), u'MeshBooleanIntersection', None, _utils.flatten(input0), _utils.flatten(input1), delete)

    def mesh_boolean_split(self, input0, input1, delete):
        """

        Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.

        Parameters

        Input0 : Required, Array, arrdbl, Array of ?
        Input1 : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(734, 1, (12, 0), ((8197, 0), (8197, 0), (11, 0),), u'MeshBooleanSplit', None, _utils.flatten(input0), _utils.flatten(input1), delete)

    def mesh_boolean_union(self, input, delete):
        """

        Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.

        Parameters

        Input : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(731, 1, (12, 0), ((8197, 0), (11, 0),), u'MeshBooleanUnion', None, _utils.flatten(input), delete)

    def mesh_closest_point(self, object, point, tolerance):
        """

        Returns the point on a mesh that is closest to a test point.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?
        Tolerance : Optional, Number, dbl, Double

        Returns

        Array : An array containing the results of the calculation, if successful. The array elements are as follows:
        Array : The 3-D point on the mesh object.
        Number : The index of the mesh face on which the 3-D point lies.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(750, 1, (12, 0), ((8, 0), (8197, 0), (5, 0),), u'MeshClosestPoint', None, object, _utils.flatten(point), tolerance)

    def mesh_contour_points(self, object, start_point, end_point, interval, remove_coincident_points):
        """

        Returns the vertices of the polyline curves generated by contouring a mesh object.

        Parameters

        Object : Required, String, str, String
        StartPoint : Required, Array, arrdbl, Array of ?
        EndPoint : Required, Array, arrdbl, Array of ?
        Interval : Optional, Number, dbl, Double
        RemoveCoincidentPoints : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of 3-D point arrays, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(123, 1, (12, 0), ((8, 0), (8197, 0), (8197, 0), (5, 0), (11, 0),), u'MeshContourPoints', None, object, _utils.flatten(start_point), _utils.flatten(end_point), interval, remove_coincident_points)

    def mesh_face_centers(self, object):
        """

        Returns the center point of each face of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of 3-D points that define the face center points of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the center points for each face return by MeshFaces.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(570, 1, (12, 0), ((8, 0),), u'MeshFaceCenters', None, object)

    def mesh_face_count(self, object):
        """

        Returns the total face count of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(124, 1, (12, 0), ((8, 0),), u'MeshFaceCount', None, object)

    def mesh_face_normals(self, object):
        """

        Returns the face unit normal for each face of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the unit normals for each face return by MeshFaces.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(569, 1, (12, 0), ((8, 0),), u'MeshFaceNormals', None, object)

    def mesh_face_vertices(self, object):
        """

        Returns the vertex indices of all faces of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array containing arrays of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(495, 1, (12, 0), ((8, 0),), u'MeshFaceVertices', None, object)

    def mesh_faces(self, object, face_type):
        """

        Returns the face vertices of a mesh object.

        Parameters

        Object : Required, String, str, String
        FaceType : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of 3-D points that define the face vertices of the mesh if successful.  If blnFaceType is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If blnFaceType is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(125, 1, (12, 0), ((8, 0), (11, 0),), u'MeshFaces', None, object, face_type)

    def mesh_has_face_normals(self, object):
        """

        Verifies a mesh object has face normals.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(696, 1, (12, 0), ((8, 0),), u'MeshHasFaceNormals', None, object)

    def mesh_has_texture_coordinates(self, object):
        """

        Verifies a mesh object has texture coordinates.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(697, 1, (12, 0), ((8, 0),), u'MeshHasTextureCoordinates', None, object)

    def mesh_has_vertex_colors(self, object):
        """

        Verifies a mesh object has vertex colors.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(698, 1, (12, 0), ((8, 0),), u'MeshHasVertexColors', None, object)

    def mesh_has_vertex_normals(self, object):
        """

        Verifies a mesh object has vertex normals.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(695, 1, (12, 0), ((8, 0),), u'MeshHasVertexNormals', None, object)

    def mesh_mesh_intersection(self, mesh1, mesh2, tolerance):
        """

        Calculates the intersection of a mesh object with another mesh object.

        Parameters

        Mesh1 : Required, String, str, String
        Mesh2 : Required, String, str, String
        Tolerance : Optional, Number, dbl, Double

        Returns

        Array : An array of 3-D point arrays that identify the vertices of the intersection curves (polylines) if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(749, 1, (12, 0), ((8, 0), (8, 0), (5, 0),), u'MeshMeshIntersection', None, mesh1, mesh2, tolerance)

    def mesh_naked_edge_points(self, object):
        """

        Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the naked status for each vertex return by MeshVertices.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(580, 1, (12, 0), ((8, 0),), u'MeshNakedEdgePoints', None, object)

    def mesh_offset(self, mesh, distance):
        """

        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.

        Parameters

        Mesh : Required, String, str, String
        Distance : Required, Number, dbl, Double

        Returns

        String : The identifier of the offset mesh object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(720, 1, (12, 0), ((8, 0), (5, 0),), u'MeshOffset', None, mesh, distance)

    def mesh_quad_count(self, object):
        """

        Returns the number of quad faces of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of quad mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(350, 1, (12, 0), ((8, 0),), u'MeshQuadCount', None, object)

    def mesh_quads_to_triangles(self, object):
        """

        Converts a mesh object's quad faces to triangles.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(352, 1, (12, 0), ((8, 0),), u'MeshQuadsToTriangles', None, object)

    def mesh_texture_coordinates(self, object):
        """

        Returns the normalized 2-D texture coordinates of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the texture coordinate for each vertex return by MeshVertices.
        Null : If the mesh does not contain texture coordinates, if not successful, or on error.

        """

        return self._ApplyTypes_(425, 1, (12, 0), ((8, 0),), u'MeshTextureCoordinates', None, object)

    def mesh_triangle_count(self, object):
        """

        Returns the number of triangular faces of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of triangular mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(351, 1, (12, 0), ((8, 0),), u'MeshTriangleCount', None, object)

    def mesh_vertex_colors(self, object, vertex_colors, null):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def mesh_vertex_count(self, object):
        """

        Returns the vertex count of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of mesh vertices if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(126, 1, (12, 0), ((8, 0),), u'MeshVertexCount', None, object)

    def mesh_vertex_normals(self, object):
        """

        Returns the vertex unit normal for each vertex of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the unit normals for each vertex return by MeshVertices.
        Null : If the mesh does not contain vertex normals, if not successful, or on error.

        """

        return self._ApplyTypes_(426, 1, (12, 0), ((8, 0),), u'MeshVertexNormals', None, object)

    def mesh_vertices(self, object):
        """

        Returns the vertices of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of 3-D points that define the vertices of the mesh if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(127, 1, (12, 0), ((8, 0),), u'MeshVertices', None, object)

    def mesh_volume(self, object, objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def mesh_volume_centroid(self, object):
        """

        Calculates the volume centroid of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : A 3-D point identifying the volume centroid if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(478, 1, (12, 0), ((8, 0),), u'MeshVolumeCentroid', None, object)

    def pull_curve_to_mesh(self, mesh, curve):
        """

        Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.

        Parameters

        Mesh : Required, String, str, String
        Curve : Required, String, str, String

        Returns

        String : The identifier of the new curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(719, 1, (12, 0), ((8, 0), (8, 0),), u'PullCurveToMesh', None, mesh, curve)

    def split_disjoint_mesh(self, object, delete):
        """

        Splits up a mesh object into its unconnected pieces.

        Parameters

        Object : Required, String, str, String
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the newly created mesh objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(722, 1, (12, 0), ((8, 0), (11, 0),), u'SplitDisjointMesh', None, object, delete)

    def unify_mesh_normals(self, object):
        """

        Fixes inconsistencies in the directions of faces of a mesh object.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of faces that were modified if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(723, 1, (12, 0), ((8, 0),), u'UnifyMeshNormals', None, object)

