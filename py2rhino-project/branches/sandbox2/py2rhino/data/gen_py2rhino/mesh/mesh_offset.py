mesh_offset = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshOffset",
    "output_package_name": "mesh",
    "output_module_name": "mesh_offset",

    "doc_html": """
        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.
    """,

    "syntax_html": """
        Rhino.MeshOffset (strMesh, dblDistance)
    """,

    "params_html": {
        0: {
            "name": "Mesh",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a mesh object.
            """
        },
        1: {
            "name": "Distance",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The distance to offset.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the offset mesh object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 720,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDistance",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

