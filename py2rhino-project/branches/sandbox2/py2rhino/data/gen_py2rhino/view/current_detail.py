current_detail = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "current_detail",

    "doc_html": """
        Returns or changes the current detail view in a page layout view.
    """,

    "syntax_html": """
        Rhino.CurrentDetail (strLayout [, strDetail [, blnReturnNames]])
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
            "name": "Detail",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title identifier of the detail view to set current.  If omitted, identifier of the current detail view is returned.  Note, if no detail views are active, then the title or identifier of the page layout view is returned. Also, to set the page layout view current, simply user strLayout as the value you pass to strDetail.
            """
        },
        2: {
            "name": "ReturnNames",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), then the name, or title, of the detail view is returned. If False, then the identifier of the detail view is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strDetail is not specified, the identifier of the current detail view if successful."
        },
        1: {
            "type": "string",
            "doc": "If strDetail is specified, the title or identifier of the previous current detail view is successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 923,

    "params_com": {
        0: {
            "name": "vaLayout",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDetail",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

