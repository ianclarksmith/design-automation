block_instance_xform = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockInstanceXform",
    "output_package_name": "block",
    "output_module_name": "block_instance_xform",

    "doc_html": """
        Returns the location of a block instance relative to the world coordinate system origin (0,0,0).  The position is returned as a 4x4 transformation matrix
    """,

    "syntax_html": """
        Rhino.BlockInstanceXform (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an existing block insertion object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A transformation matrix (4x4 array of numbers) if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 415,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

