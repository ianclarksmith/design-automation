view_names = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewNames",
    "output_package_name": "view",
    "output_module_name": "view_names",

    "doc_html": """
        Returns the names, or titles, or identifiers of all views in the document.
    """,

    "syntax_html": """
        Rhino.ViewNames ([blnReturnNames [, intType]])
    """,

    "params_html": {
        0: {
            "name": "ReturnNames",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), then the names, or titles, of the views are returned. If False, then the identifiers of the views are returned.
            """
        },
        1: {
            "name": "Type",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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

