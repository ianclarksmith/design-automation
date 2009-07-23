delete_named_c_plane = {
    "input_folder_name": "View_Methods",
    "input_file_name": "DeleteNamedCPlane",
    "output_package_name": "view",
    "output_module_name": "delete_named_c_plane",

    "doc_html": """
        Removed a new named construction plane from the document.
    """,

    "syntax_html": {
        0: ("strName"),
    },

    "params_html": {
        0: {
            "name": "strName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
            "doc": """
        The name of the named construction plane to remove.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 284,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

