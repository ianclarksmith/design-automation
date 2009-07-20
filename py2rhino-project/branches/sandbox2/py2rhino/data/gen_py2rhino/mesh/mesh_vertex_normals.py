mesh_vertex_normals = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshVertexNormals",
    "output_package_name": "mesh",
    "output_module_name": "mesh_vertex_normals",

    "doc_html": """
        Returns the vertex unit normal for each vertex of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshVertexNormals (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a mesh object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the unit normals for each vertex return by MeshVertices."
        },
        1: {
            "type": "null",
            "doc": "If the mesh does not contain vertex normals, if not successful, or on error."
        },
    },

    "id_com": 426,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

