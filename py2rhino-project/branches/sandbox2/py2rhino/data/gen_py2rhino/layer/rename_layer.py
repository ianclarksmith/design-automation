rename_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "RenameLayer",
    "output_package_name": "layer",
    "output_module_name": "rename_layer",

    "doc_html": """
        Renames an existing layer.
    """,

    "syntax_html": """
        Rhino.RenameLayer (strOldName, strNewName)
    """,

    "params_html": {
        0: {
            "name": "OldName",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing layer.
            """
        },
        1: {
            "name": "NewName",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new layer name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The new layer name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 16,

    "params_com": {
        0: {
            "name": "vaOld",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNew",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

