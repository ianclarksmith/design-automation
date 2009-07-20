mesh_vertex_colors = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshVertexColors",
    "output_package_name": "mesh",
    "output_module_name": "mesh_vertex_colors",

    "doc_html": """
        Returns or modifies the  vertex colors of a mesh object
    """,

    "syntax_html": """
        Rhino.MeshVertexColors (strObject [, arrVertexColors])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "VertexColors",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
            """
        },
        2: {
            "name": "Null",
            "opt_or_req": "Optional",
            "type": "Null",
            "type_string": "arr",
            "doc": """
        Specifying Null will remove, or purge, any existing vertex colors from the mesh.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrVertexColors  is not specified,  the current vertex color if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrVertexColors  is specified, the previous vertex colors if successful."
        },
        2: {
            "type": "null",
            "doc": "If strObject does not have vertex colors, if not successful, or on error."
        },
    },

    "id_com": 699,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaColors",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
