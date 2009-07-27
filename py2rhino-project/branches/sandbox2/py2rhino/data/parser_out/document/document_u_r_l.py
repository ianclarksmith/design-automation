document_u_r_l = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "DocumentURL",
    "output_package_name": "document",
    "output_module_name": "document_u_r_l",

    "doc_html": """
        Returns or sets the uniform resource locator (URL) of the currently loaded Rhino document (3DM file).
    """,

    "syntax_html": {
        0: ("strURL"),
    },

    "params_html": {
        0: {
            "name": "strURL",
            "py_name": "u_r_l",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "URL",
            "doc": """
        The URL.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If no URL is specified, the current URL if successful."
        },
        1: {
            "type": "string",
            "doc": "If a URL is specified, the previous URL if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 275,

    "params_com": {
        0: {
            "name": "vaURL",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

