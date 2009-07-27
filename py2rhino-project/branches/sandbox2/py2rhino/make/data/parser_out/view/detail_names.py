detail_names = {
    "input_folder_name": "View_Methods",
    "input_file_name": "DetailNames",
    "output_package_name": "view",
    "output_module_name": "detail_names",

    "doc_html": """
        Returns the names, or titles, or identifiers of all detail views in a page layout view.
    """,

    "syntax_html": {
        0: ("strLayout", "blnReturnNames"),
    },

    "params_html": {
        0: {
            "name": "strLayout",
            "py_name": "layout",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layout",
            "doc": """
        The title or identifier of an existing page layout view.
            """
        },
        1: {
            "name": "blnReturnNames",
            "py_name": "return_names",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnNames",
            "doc": """
        If True (default), then the names, or titles, of the detail views are returned. If False, then the identifiers of the detail views are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A array of strings identifying the detail view names, or titles, or identifiers if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 922,

    "params_com": {
        0: {
            "name": "vaLayout",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

