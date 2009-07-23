add_mesh = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "AddMesh",
    "output_package_name": "mesh",
    "output_module_name": "add_mesh",

    "doc_html": """
        Adds a mesh object to the document.
    """,

    "syntax_html": {
        0: ("arrVertices", "arrFaceVertices", "arrVertexNormals", "arrTextureCoordinates", "arrVertexColors"),
    },

    "params_html": {
        0: {
            "name": "arrVertices",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vertices",
            "doc": """
        An array of 3-D points defining the vertices of the mesh.
            """
        },
        1: {
            "name": "arrFaceVertices",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "FaceVertices",
            "doc": """
        An array containing arrays of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
            """
        },
        2: {
            "name": "arrVertexNormals",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "VertexNormals",
            "doc": """
        An array of 3-D vectors defining the vertex normals of the mesh. Note, for every vertex, the must be a corresponding vertex normal.
            """
        },
        3: {
            "name": "arrTextureCoordinates",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "TextureCoordinates",
            "doc": """
        An array of 2-D texture coordinates. Note, for every vertex, there must be a corresponding texture coordinate.
            """
        },
        4: {
            "name": "arrVertexColors",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "VertexColors",
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

