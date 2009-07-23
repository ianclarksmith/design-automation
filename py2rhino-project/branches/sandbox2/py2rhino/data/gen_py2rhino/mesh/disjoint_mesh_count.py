disjoint_mesh_count = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "DisjointMeshCount",
    "output_package_name": "mesh",
    "output_module_name": "disjoint_mesh_count",

    "doc_html": """
        Returns the number of meshes that could be created by calling SplitDisjointMesh.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a mesh object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of meshes that could be created if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 721,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

