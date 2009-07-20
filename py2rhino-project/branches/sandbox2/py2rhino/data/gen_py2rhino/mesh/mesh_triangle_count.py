mesh_triangle_count = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshTriangleCount",
    "output_package_name": "mesh",
    "output_module_name": "mesh_triangle_count",

    "doc_html": """
        Returns the number of triangular faces of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshTriangleCount (strObject)
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
            "type": "number",
            "doc": "The number of triangular mesh faces if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 351,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

