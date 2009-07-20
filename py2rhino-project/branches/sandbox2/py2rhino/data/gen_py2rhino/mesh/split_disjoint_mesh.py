split_disjoint_mesh = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "SplitDisjointMesh",
    "output_package_name": "mesh",
    "output_module_name": "split_disjoint_mesh",

    "doc_html": """
        Splits up a mesh object into its unconnected pieces.
    """,

    "syntax_html": """
        Rhino.SplitDisjointMesh (strObject [, blnDelete])
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
        1: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

