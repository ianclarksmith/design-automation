mesh_vertex_colors = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshVertexColors",
    "output_package_name": "mesh",
    "output_module_name": "mesh_vertex_colors",

    "doc_html": """
        Returns or modifies the  vertex colors of a mesh object
    """,

    "syntax_html": {
        0: ("strObject", "arrVertexColors"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "arrVertexColors",
            "py_name": "vertex_colors",
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

