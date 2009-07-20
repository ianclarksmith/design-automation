mesh_has_vertex_colors = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshHasVertexColors",
    "output_package_name": "mesh",
    "output_module_name": "mesh_has_vertex_colors",

    "doc_html": """
        Verifies a mesh object has vertex colors.
    """,

    "syntax_html": """
        Rhino.MeshHasVertexColors (strObject)
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
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 698,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
