view_title = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_title",

    "doc_html": """
        Returns the name, or title, of a view given a view's identifier.
    """,

    "syntax_html": """
        Rhino.ViewTitle (strView])
    """,

    "params_html": {
        0: {
            "name": "Mode",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the display mode obtained from the ViewNames method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name, or title, of the view if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 907,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

