# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Mesh(DispatchBaseClass):



    def addmesh(self, arrvertices, arrfacevertices, arrvertexnormals, arrtexturecoordinates, arrvertexcolors):
        """

        Adds a mesh object to the document.

        Parameters

        arrVertices : Required,  Array,   An array of 3-D points defining the vertices of the mesh
        arrFaceVertices : Required,  Array,   An array containing arrays of four numbers that define the vertex indices for each face of the mesh
        arrVertexNormals : Optional,  Array,   An array of 3-D vectors defining the vertex normals of the mesh
        arrTextureCoordinates : Optional,  Array,  An array of 2-D texture coordinates
        arrVertexColors : Optional,   Array,   An array of RGB color values

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddMesh', None, arrVertices, arrFaceVertices, arrVertexNormals, arrTextureCoordinates, arrVertexColors)

    def addplanarmesh(self, strobject, blndelete):
        """

        Creates a planar mesh from a closed, planar curve.

        Parameters

        strObject : Required,   String,   The identifier of a closed, planar curve object
        blnDelete : Required,   Boolean,   If True, then the input curve will be deleted

        Returns

        String : An string identifying the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPlanarMesh', None, strObject, blnDelete)

    def curvemeshintersect(self, strcurve, strmesh, blnreturnfaces):
        """

        Calculates the intersection of a curve object and a mesh object.

        Parameters

        strCurve : Required,   String,   The identifier of the curve to intersect
        strMesh : Required,   String,   The identifier of the mesh to intersect
        blnReturnFaces : Optional,   Boolean,   Return both intersection points and face indices

        Returns

        Array : If blnReturnFaces is either omitted or False, then an array intersection points, if successful.
        Array : If blnReturnFaces is True, then a one-dimensional array containing information about each intersection if successful.  Each array element is a one-dimensional array that contains the following two elements:
        Array : The 3-D intersection point.
        Number : The mesh face index on which the intersection point lies.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveMeshIntersect', None, strCurve, strMesh, blnReturnFaces)

    def disjointmeshcount(self, strobject):
        """

        Returns the number of meshes that could be created by calling SplitDisjointMesh.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of meshes that could be created if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DisjointMeshCount', None, strObject)

    def duplicatemeshborder(self, strobject):
        """

        Creates a curve that duplicates a mesh border.

        Parameters

        strObject : Required,   String,   The identifier of the mesh object

        Returns

        Array : An array of strings identifying the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DuplicateMeshBorder', None, strObject)

    def explodemeshes(self, strobject, arrobjects, blndelete):
        """

        Explodes a mesh object, or mesh objects,  into submeshes.  A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges.  Unwelded mesh edges are edges where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge.

        Parameters

        strObject : Required,   String,   The identifier of the mesh object to explode
        arrObjects : Required,   Array,    An array of strings identifying the mesh objects to explode
        blnDelete : Optional,   Boolean,   Delete input objects after exploding

        Returns

        Array : An array of strings identifying the newly created mesh objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExplodeMeshes', None, strObject, arrObjects, blnDelete)

    def ismesh(self, strobject):
        """

        Verifies an object is a mesh object.

        Parameters

        strObject : Required,  String,  The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsMesh', None, strObject)

    def ismeshclosed(self, strobject):
        """

        Verifies a mesh object is closed.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsMeshClosed', None, strObject)

    def ismeshmanifold(self, strobject):
        """

        Verifies a mesh object is manifold.  A mesh for which every edge is shared by at most two faces is called a manifold.  If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsMeshManifold', None, strObject)

    def mesharea(self, strobject, arrobjects):
        """

        Returns the approximate area of one or more mesh objects.

        Parameters

        strObject : Required,   String,   The object's identifier
        arrObjects : Required,   Array,   An array of object identifier

        Returns

        Array : An array containing three numbers if successful.  The three elements of the array are as follows:
        Number : The number of meshes used in the area calculation.
        Number : The total area of all meshes.
        Number : The error estimate.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshArea', None, strObject, arrObjects)

    def meshareacentroid(self, strobject):
        """

        Calculates the area centroid of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : A 3-D point identifying the area centroid if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshAreaCentroid', None, strObject)

    def meshbooleandifference(self, arrinput0, arrinput1, blndelete):
        """

        Performs a Boolean difference operation on two sets of input meshes. For more details, see the MeshBooleanDifference command in the Rhino help file.

        Parameters

        arrInput0 : Required,   Array,   The identifiers of the meshes
        arrInput1 : Required,   Array,   The identifiers of the meshes
        blnDelete : Optional,   Boolean,  Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshBooleanDifference', None, arrInput0, arrInput1, blnDelete)

    def meshbooleanintersection(self, arrinput0, arrinput1, blndelete):
        """

        Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.

        Parameters

        arrInput0 : Required,   Array,   The identifiers of the meshes
        arrInput1 : Required,   Array,   The identifiers of the meshes
        blnDelete : Optional,   Boolean,  Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshBooleanIntersection', None, arrInput0, arrInput1, blnDelete)

    def meshbooleansplit(self, arrinput0, arrinput1, blndelete):
        """

        Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.

        Parameters

        arrInput0 : Required,   Array,   The identifiers of the meshes
        arrInput1 : Required,   Array,   The identifiers of the meshes
        blnDelete : Optional,   Boolean,  Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshBooleanSplit', None, arrInput0, arrInput1, blnDelete)

    def meshbooleanunion(self, arrinput, blndelete):
        """

        Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.

        Parameters

        arrInput : Required,   Array,   The identifiers of the meshes to union
        blnDelete : Optional,   Boolean,  Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshBooleanUnion', None, arrInput, blnDelete)

    def meshclosestpoint(self, strobject, arrpoint, dbltolerance):
        """

        Returns the point on a mesh that is closest to a test point.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object
        arrPoint : Required,   Array,   A 3-D point to test
        dblTolerance : Optional,   Number,   The tolerance

        Returns

        Array : An array containing the results of the calculation, if successful. The array elements are as follows:
        Array : The 3-D point on the mesh object.
        Number : The index of the mesh face on which the 3-D point lies.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshClosestPoint', None, strObject, arrPoint, dblTolerance)

    def meshcontourpoints(self, strobject, arrstartpoint, arrendpoint, dblinterval, blnremovecoincidentpoints):
        """

        Returns the vertices of the polyline curves generated by contouring a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object
        arrStartPoint : Required,   Array,   The 3-D starting point of a center line
        arrEndPoint : Required,   Array,   The 3-D ending point of a center line
        dblInterval : Optional,   Number,   The distance between contour curves
        blnRemoveCoincidentPoints : Optional,   Boolean,   Remove coincident points

        Returns

        Array : An array of 3-D point arrays, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshContourPoints', None, strObject, arrStartPoint, arrEndPoint, dblInterval, blnRemoveCoincidentPoints)

    def meshfacecenters(self, strobject):
        """

        Returns the center point of each face of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of 3-D points that define the face center points of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the center points for each face return by MeshFaces.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshFaceCenters', None, strObject)

    def meshfacecount(self, strobject):
        """

        Returns the total face count of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshFaceCount', None, strObject)

    def meshfacenormals(self, strobject):
        """

        Returns the face unit normal for each face of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the unit normals for each face return by MeshFaces.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshFaceNormals', None, strObject)

    def meshfacevertices(self, strobject):
        """

        Returns the vertex indices of all faces of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array containing arrays of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshFaceVertices', None, strObject)

    def meshfaces(self, strobject, blnfacetype):
        """

        Returns the face vertices of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object
        blnFaceType : Optional,   Boolean,   The face type to be returned

        Returns

        Array : An array of 3-D points that define the face vertices of the mesh if successful.  If blnFaceType is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If blnFaceType is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshFaces', None, strObject, blnFaceType)

    def meshhasfacenormals(self, strobject):
        """

        Verifies a mesh object has face normals.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshHasFaceNormals', None, strObject)

    def meshhastexturecoordinates(self, strobject):
        """

        Verifies a mesh object has texture coordinates.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshHasTextureCoordinates', None, strObject)

    def meshhasvertexcolors(self, strobject):
        """

        Verifies a mesh object has vertex colors.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshHasVertexColors', None, strObject)

    def meshhasvertexnormals(self, strobject):
        """

        Verifies a mesh object has vertex normals.

        Parameters

        strObject : Required,   String,   The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshHasVertexNormals', None, strObject)

    def meshmeshintersection(self, strmesh1, strmesh2, dbltolerance):
        """

        Calculates the intersection of a mesh object with another mesh object.

        Parameters

        strMesh1 : Required,   String,   The identifier of the first mesh object
        strMesh2 : Required,   String,   The identifier of the second mesh object
        dblTolerance : Optional,   Number,   The intersection tolerance

        Returns

        Array : An array of 3-D point arrays that identify the vertices of the intersection curves (polylines) if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshMeshIntersection', None, strMesh1, strMesh2, dblTolerance)

    def meshnakededgepoints(self, strobject):
        """

        Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the naked status for each vertex return by MeshVertices.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshNakedEdgePoints', None, strObject)

    def meshoffset(self, strmesh, dbldistance):
        """

        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.

        Parameters

        strMesh : Required,   String,   The identifier of a mesh object
        dblDistance : Required,   Number,   The distance to offset

        Returns

        String : The identifier of the offset mesh object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshOffset', None, strMesh, dblDistance)

    def meshquadcount(self, strobject):
        """

        Returns the number of quad faces of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of quad mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshQuadCount', None, strObject)

    def meshquadstotriangles(self, strobject):
        """

        Converts a mesh object's quad faces to triangles.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshQuadsToTriangles', None, strObject)

    def meshtexturecoordinates(self, strobject):
        """

        Returns the normalized 2-D texture coordinates of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the texture coordinate for each vertex return by MeshVertices.
        Null : If the mesh does not contain texture coordinates, if not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshTextureCoordinates', None, strObject)

    def meshtrianglecount(self, strobject):
        """

        Returns the number of triangular faces of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of triangular mesh faces if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshTriangleCount', None, strObject)

    def meshvertexcolors(self, strobject, arrvertexcolors, null):
        """

        Returns or modifies the  vertex colors of a mesh object

        Parameters

        strObject : Required,   String,   The object's identifier
        arrVertexColors : Optional,   Array,   An array of RGB color values
        Null : Optional,   Null,   Specifying Null will remove, or purge, any existing vertex colors from the mesh

        Returns

        Array : If arrVertexColors  is not specified,  the current vertex color if successful.
        Array : If arrVertexColors  is specified, the previous vertex colors if successful.
        Null : If strObject does not have vertex colors, if not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVertexColors', None, strObject, arrVertexColors, Null)

    def meshvertexcount(self, strobject):
        """

        Returns the vertex count of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of mesh vertices if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVertexCount', None, strObject)

    def meshvertexnormals(self, strobject):
        """

        Returns the vertex unit normal for each vertex of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the unit normals for each vertex return by MeshVertices.
        Null : If the mesh does not contain vertex normals, if not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVertexNormals', None, strObject)

    def meshvertices(self, strobject):
        """

        Returns the vertices of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : An array of 3-D points that define the vertices of the mesh if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVertices', None, strObject)

    def meshvolume(self, strobject, arrobjects):
        """

        Returns the approximate volume of one or more closed mesh objects.

        Parameters

        strObject : Required,   String,   The object's identifier
        arrObjects : Required,   Array,   An array of object identifier

        Returns

        Array : An array containing three numbers if successful.  The three elements of the array are as follows:
        Number : The number of meshes used in the volume calculation.
        Number : The total volume of all meshes.
        Number : The error estimate.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVolume', None, strObject, arrObjects)

    def meshvolumecentroid(self, strobject):
        """

        Calculates the volume centroid of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Array : A 3-D point identifying the volume centroid if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshVolumeCentroid', None, strObject)

    def pullcurvetomesh(self, strmesh, strcurve):
        """

        Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.

        Parameters

        strMesh : Required,   String,   The identifier of the mesh object that pulls
        strCurve : Required,   String,   The identifier of the curve object to pull

        Returns

        String : The identifier of the new curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PullCurveToMesh', None, strMesh, strCurve)

    def splitdisjointmesh(self, strobject, blndelete):
        """

        Splits up a mesh object into its unconnected pieces.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object
        blnDelete : Optional,   Boolean,   Delete the input object

        Returns

        Array : An array of strings identifying the newly created mesh objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SplitDisjointMesh', None, strObject, blnDelete)

    def unifymeshnormals(self, strobject):
        """

        Fixes inconsistencies in the directions of faces of a mesh object.

        Parameters

        strObject : Required,   String,   The identifier of a mesh object

        Returns

        Number : The number of faces that were modified if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnifyMeshNormals', None, strObject)

