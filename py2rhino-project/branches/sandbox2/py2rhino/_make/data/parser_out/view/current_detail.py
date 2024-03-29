current_detail = {
    "input_folder_name": "View_Methods",
    "input_file_name": "CurrentDetail",
    "output_package_name": "view",
    "output_module_name": "current_detail",

    "doc_html": """
        Returns or changes the current detail view in a page layout view.
    """,

    "syntax_html": {
        0: ("strLayout", "strDetail", "blnReturnNames"),
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
            "name": "strDetail",
            "py_name": "detail",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Detail",
            "doc": """
        The title identifier of the detail view to set current.  If omitted, identifier of the current detail view is returned.  Note, if no detail views are active, then the title or identifier of the page layout view is returned. Also, to set the page layout view current, simply user strLayout as the value you pass to strDetail.
            """
        },
        2: {
            "name": "blnReturnNames",
            "py_name": "return_names",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnNames",
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

