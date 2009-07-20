detail_names = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "detail_names",

    "doc_html": """
        Returns the names, or titles, or identifiers of all detail views in a page layout view.
    """,

    "syntax_html": """
        Rhino.DetailNames (strLayout [,blnReturnNames])
    """,

    "params_html": {
        0: {
            "name": "Layout",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of an existing page layout view.
            """
        },
        1: {
            "name": "ReturnNames",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

