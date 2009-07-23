split_disjoint_mesh = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "SplitDisjointMesh",
    "output_package_name": "mesh",
    "output_module_name": "split_disjoint_mesh",

    "doc_html": """
        Splits up a mesh object into its unconnected pieces.
    """,

    "syntax_html": {
        0: ("strObject", "blnDelete"),
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
        1: {
            "name": "blnDelete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete the input object. The default is not to delete the input object (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created mesh objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 722,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

