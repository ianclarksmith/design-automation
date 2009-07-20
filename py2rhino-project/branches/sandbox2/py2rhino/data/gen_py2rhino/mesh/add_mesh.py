add_mesh = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "add_mesh",

    "doc_html": """
        Adds a mesh object to the document.
    """,

    "syntax_html": """
        Rhino.AddMesh (arrVertices, arrFaceVertices [, arrVertexNormals [, arrTextureCoordinates [, arrVertexColors ]]])
    """,

    "params_html": {
        0: {
            "name": "Vertices",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points defining the vertices of the mesh.
            """
        },
        1: {
            "name": "FaceVertices",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array containing arrays of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
            """
        },
        2: {
            "name": "VertexNormals",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D vectors defining the vertex normals of the mesh. Note, for every vertex, the must be a corresponding vertex normal.
            """
        },
        3: {
            "name": "TextureCoordinates",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 2-D texture coordinates. Note, for every vertex, there must be a corresponding texture coordinate.
            """
        },
        4: {
            "name": "VertexColors",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 494,

    "params_com": {
        0: {
            "name": "vaVertices",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFaces",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaNormals",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaTextures",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaColors",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

