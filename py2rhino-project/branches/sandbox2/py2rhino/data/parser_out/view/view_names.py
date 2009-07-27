view_names = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewNames",
    "output_package_name": "view",
    "output_module_name": "view_names",

    "doc_html": """
        Returns the names, or titles, or identifiers of all views in the document.
    """,

    "syntax_html": {
        0: ("blnReturnNames", "intType"),
    },

    "params_html": {
        0: {
            "name": "blnReturnNames",
            "py_name": "return_names",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnNames",
            "doc": """
        If True (default), then the names, or titles, of the views are returned. If False, then the identifiers of the views are returned.
            """
        },
        1: {
            "name": "intType",
            "py_name": "type",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Type",
            "doc": """
        The type of view to return, where:
		Value
		Description
		0
		Standard model views.
		1
		Page layout views.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A array of strings identifying the view names, or titles, or identifiers if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 265,

    "params_com": {
        0: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTypes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

