mesh_naked_edge_points = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshNakedEdgePoints",
    "output_package_name": "mesh",
    "output_module_name": "mesh_naked_edge_points",

    "doc_html": """
        Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.
    """,

    "syntax_html": """
        Rhino.MeshNakedEdgePoints (strObject)
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
            "doc": "An array of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the naked status for each vertex return by MeshVertices."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 580,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

