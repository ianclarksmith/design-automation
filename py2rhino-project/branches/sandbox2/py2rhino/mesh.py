# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Mesh(IRhinoScript):



    def add_mesh(self, vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors):
        """        
        Adds a mesh object to the document.
    
        Parameters
        ==========

        vertices, Array of ????, Required        
        An array of 3-D points defining the vertices of the mesh.
            
        face_vertices, Array of ????, Required        
        An array containing arrays of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
            
        vertex_normals, Array of ????, Optional        
        An array of 3-D vectors defining the vertex normals of the mesh. Note, for every vertex, the must be a corresponding vertex normal.
            
        texture_coordinates, Array of ????, Optional        
        An array of 2-D texture coordinates. Note, for every vertex, there must be a corresponding texture coordinate.
            
        vertex_colors, Array of ????, Optional        
        An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(494, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddMesh", None, flatten(vertices), flatten(face_vertices), flatten(vertex_normals), flatten(texture_coordinates), flatten(vertex_colors))

    def add_planar_mesh(self, object, delete):
        """        
        Creates a planar mesh from a closed, planar curve.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a closed, planar curve object.
            
        delete, Boolean, Required        
        If True, then the input curve will be deleted. If not specified or False (default), then the input curve will not be deleted.
            
        Returns
        =======

        string
        An string identifying the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(915, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"AddPlanarMesh", None, object, delete)

    def curve_mesh_intersection(self, curve, mesh, return_faces):
        """        
        Calculates the intersection of a curve object and a mesh object.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve to intersect.
            
        mesh, String, Required        
        The identifier of the mesh to intersect.
            
        return_faces, Boolean, Optional        
        Return both intersection points and face indices.  If omitted or False, then just the intersection points are returned.
            
        Returns
        =======

        array
        If blnReturnFaces is either omitted or False, then an array intersection points, if successful.

        array
        If blnReturnFaces is True, then a one-dimensional array containing information about each intersection if successful.  Each array element is a one-dimensional array that contains the following two elements:

        array
        The 3-D intersection point.

        number
        The mesh face index on which the intersection point lies.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(842, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)), u"CurveMeshIntersection", None, curve, mesh, return_faces)

    def disjoint_mesh_count(self, object):
        """        
        Returns the number of meshes that could be created by calling SplitDisjointMesh.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of meshes that could be created if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(721, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"DisjointMeshCount", None, object)

    def duplicate_mesh_border(self, object):
        """        
        Creates a curve that duplicates a mesh border.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the mesh object.
            
        Returns
        =======

        array
        An array of strings identifying the new curve objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(853, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"DuplicateMeshBorder", None, object)

    def explode_meshes(self, object, objects, delete):
        """        
        Explodes a mesh object, or mesh objects,  into submeshes.  A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges.  Unwelded mesh edges are edges where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the mesh object to explode.
            
        objects, Array of ????, Required        
        An array of strings identifying the mesh objects to explode.
            
        delete, Boolean, Optional        
        Delete input objects after exploding.  The default is not to delete objects (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created mesh objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(903, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"ExplodeMeshes", None, object, flatten(objects), delete)

    def is_mesh(self, object):
        """        
        Verifies an object is a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(119, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsMesh", None, object)

    def is_mesh_closed(self, object):
        """        
        Verifies a mesh object is closed.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(355, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsMeshClosed", None, object)

    def is_mesh_manifold(self, object):
        """        
        Verifies a mesh object is manifold.  A mesh for which every edge is shared by at most two faces is called a manifold.  If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(855, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsMeshManifold", None, object)

    def mesh_area(self, object, objects):
        """        
        Returns the approximate area of one or more mesh objects.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        objects, Array of ????, Required        
        An array of object identifier.
            
        Returns
        =======

        array
        An array containing three numbers if successful.  The three elements of the array are as follows:

        number
        The number of meshes used in the area calculation.

        number
        The total area of all meshes.

        number
        The error estimate.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(353, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"MeshArea", None, object, flatten(objects))

    def mesh_area_centroid(self, object):
        """        
        Calculates the area centroid of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        A 3-D point identifying the area centroid if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(477, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshAreaCentroid", None, object)

    def mesh_boolean_difference(self, input0, input1, delete):
        """        
        Performs a Boolean difference operation on two sets of input meshes. For more details, see the MeshBooleanDifference command in the Rhino help file.
    
        Parameters
        ==========

        input0, Array of ????, Required        
        The identifiers of the meshes.
            
        input1, Array of ????, Required        
        The identifiers of the meshes.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(732, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"MeshBooleanDifference", None, flatten(input0), flatten(input1), delete)

    def mesh_boolean_intersection(self, input0, input1, delete):
        """        
        Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.
    
        Parameters
        ==========

        input0, Array of ????, Required        
        The identifiers of the meshes.
            
        input1, Array of ????, Required        
        The identifiers of the meshes.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(733, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"MeshBooleanIntersection", None, flatten(input0), flatten(input1), delete)

    def mesh_boolean_split(self, input0, input1, delete):
        """        
        Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.
    
        Parameters
        ==========

        input0, Array of ????, Required        
        The identifiers of the meshes.
            
        input1, Array of ????, Required        
        The identifiers of the meshes.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(734, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"MeshBooleanSplit", None, flatten(input0), flatten(input1), delete)

    def mesh_boolean_union(self, input, delete):
        """        
        Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.
    
        Parameters
        ==========

        input, Array of ????, Required        
        The identifiers of the meshes to union.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(731, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BOOL, 1)), u"MeshBooleanUnion", None, flatten(input), delete)

    def mesh_closest_point(self, object, point, tolerance):
        """        
        Returns the point on a mesh that is closest to a test point.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        point, Array of ????, Required        
        A 3-D point to test.
            
        tolerance, Double, Optional        
        The tolerance. Of omitted, a default tolerance of 0.0 is used.
            
        Returns
        =======

        array
        An array containing the results of the calculation, if successful. The array elements are as follows:

        array
        The 3-D point on the mesh object.

        number
        The index of the mesh face on which the 3-D point lies.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(750, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"MeshClosestPoint", None, object, flatten(point), tolerance)

    def mesh_contour_points(self, object, start_point, end_point, interval, remove_coincident_points):
        """        
        Returns the vertices of the polyline curves generated by contouring a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        start_point, Array of ????, Required        
        The 3-D starting point of a center line.
            
        end_point, Array of ????, Required        
        The 3-D ending point of a center line.
            
        interval, Double, Optional        
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            
        remove_coincident_points, Boolean, Optional        
        Remove coincident points.  If True, and the polyline curves from which the contour point are taken are closed, then duplicate starting and ending points of the polyline curve will not be returned. The default is to return duplicate starting and ending points (False).
            
        Returns
        =======

        array
        An array of 3-D point arrays, one for each contour, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(123, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BOOL, 1)), u"MeshContourPoints", None, object, flatten(start_point), flatten(end_point), interval, remove_coincident_points)

    def mesh_face_centers(self, object):
        """        
        Returns the center point of each face of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of 3-D points that define the face center points of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the center points for each face return by MeshFaces.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(570, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshFaceCenters", None, object)

    def mesh_face_count(self, object):
        """        
        Returns the total face count of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of mesh faces if successful

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(124, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshFaceCount", None, object)

    def mesh_face_normals(self, object):
        """        
        Returns the face unit normal for each face of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the unit normals for each face return by MeshFaces.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(569, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshFaceNormals", None, object)

    def mesh_face_vertices(self, object):
        """        
        Returns the vertex indices of all faces of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array containing arrays of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(495, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshFaceVertices", None, object)

    def mesh_faces(self, object, face_type):
        """        
        Returns the face vertices of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        face_type, Boolean, Optional        
        The face type to be returned.  If omitted, both triangles and quads are returned (True)
		Value
		Description
		True
		Both triangles and quads.
		False
            
        Returns
        =======

        array
        An array of 3-D points that define the face vertices of the mesh if successful.  If blnFaceType is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If blnFaceType is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(125, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"MeshFaces", None, object, face_type)

    def mesh_has_face_normals(self, object):
        """        
        Verifies a mesh object has face normals.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(696, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshHasFaceNormals", None, object)

    def mesh_has_texture_coordinates(self, object):
        """        
        Verifies a mesh object has texture coordinates.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(697, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshHasTextureCoordinates", None, object)

    def mesh_has_vertex_colors(self, object):
        """        
        Verifies a mesh object has vertex colors.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(698, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshHasVertexColors", None, object)

    def mesh_has_vertex_normals(self, object):
        """        
        Verifies a mesh object has vertex normals.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(695, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshHasVertexNormals", None, object)

    def mesh_mesh_intersection(self, mesh1, mesh2, tolerance):
        """        
        Calculates the intersection of a mesh object with another mesh object.
    
        Parameters
        ==========

        mesh1, String, Required        
        The identifier of the first mesh object.
            
        mesh2, String, Required        
        The identifier of the second mesh object.
            
        tolerance, Double, Optional        
        The intersection tolerance. Of omitted, Rhino's internal zero tolerance is used.
            
        Returns
        =======

        array
        An array of 3-D point arrays that identify the vertices of the intersection curves (polylines) if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(749, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)), u"MeshMeshIntersection", None, mesh1, mesh2, tolerance)

    def mesh_naked_edge_points(self, object):
        """        
        Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the naked status for each vertex return by MeshVertices.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(580, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshNakedEdgePoints", None, object)

    def mesh_offset(self, mesh, distance):
        """        
        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.
    
        Parameters
        ==========

        mesh, String, Required        
        The identifier of a mesh object.
            
        distance, Double, Required        
        The distance to offset.
            
        Returns
        =======

        string
        The identifier of the offset mesh object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(720, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"MeshOffset", None, mesh, distance)

    def mesh_quad_count(self, object):
        """        
        Returns the number of quad faces of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of quad mesh faces if successful

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(350, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshQuadCount", None, object)

    def mesh_quads_to_triangles(self, object):
        """        
        Converts a mesh object's quad faces to triangles.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(352, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshQuadsToTriangles", None, object)

    def mesh_texture_coordinates(self, object):
        """        
        Returns the normalized 2-D texture coordinates of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the texture coordinate for each vertex return by MeshVertices.

        null
        If the mesh does not contain texture coordinates, if not successful, or on error.

        """

        return self._ApplyTypes_(425, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshTextureCoordinates", None, object)

    def mesh_triangle_count(self, object):
        """        
        Returns the number of triangular faces of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of triangular mesh faces if successful

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(351, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshTriangleCount", None, object)

    def mesh_vertex_colors(self, object, vertex_colors, null):
        """        
        Returns or modifies the  vertex colors of a mesh object
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        vertex_colors, Array of ????, Optional        
        An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
            
        null, Array of ????, Optional        
        Specifying Null will remove, or purge, any existing vertex colors from the mesh.
            
        Returns
        =======

        array
        If arrVertexColors  is not specified,  the current vertex color if successful.

        array
        If arrVertexColors  is specified, the previous vertex colors if successful.

        null
        If strObject does not have vertex colors, if not successful, or on error.

        """

        return self._ApplyTypes_(699, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"MeshVertexColors", None, object, flatten(vertex_colors), flatten(null))

    def mesh_vertex_count(self, object):
        """        
        Returns the vertex count of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of mesh vertices if successful

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(126, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshVertexCount", None, object)

    def mesh_vertex_normals(self, object):
        """        
        Returns the vertex unit normal for each vertex of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the unit normals for each vertex return by MeshVertices.

        null
        If the mesh does not contain vertex normals, if not successful, or on error.

        """

        return self._ApplyTypes_(426, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshVertexNormals", None, object)

    def mesh_vertices(self, object):
        """        
        Returns the vertices of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        An array of 3-D points that define the vertices of the mesh if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(127, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshVertices", None, object)

    def mesh_volume(self, object, objects):
        """        
        Returns the approximate volume of one or more closed mesh objects.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        objects, Array of ????, Required        
        An array of object identifier.
            
        Returns
        =======

        array
        An array containing three numbers if successful.  The three elements of the array are as follows:

        number
        The number of meshes used in the volume calculation.

        number
        The total volume of all meshes.

        number
        The error estimate.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(354, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"MeshVolume", None, object, flatten(objects))

    def mesh_volume_centroid(self, object):
        """        
        Calculates the volume centroid of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        array
        A 3-D point identifying the volume centroid if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(478, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshVolumeCentroid", None, object)

    def pull_curve_to_mesh(self, mesh, curve):
        """        
        Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.
    
        Parameters
        ==========

        mesh, String, Required        
        The identifier of the mesh object that pulls.
            
        curve, String, Required        
        The identifier of the curve object to pull.
            
        Returns
        =======

        string
        The identifier of the new curve object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(719, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"PullCurveToMesh", None, mesh, curve)

    def split_disjoint_mesh(self, object, delete):
        """        
        Splits up a mesh object into its unconnected pieces.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        delete, Boolean, Optional        
        Delete the input object. The default is not to delete the input object (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created mesh objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(722, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"SplitDisjointMesh", None, object, delete)

    def unify_mesh_normals(self, object):
        """        
        Fixes inconsistencies in the directions of faces of a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a mesh object.
            
        Returns
        =======

        number
        The number of faces that were modified if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(723, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"UnifyMeshNormals", None, object)

