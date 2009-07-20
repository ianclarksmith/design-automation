view_radius = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_radius",

    "doc_html": """
        Returns or sets the radius of the viewing frustum of a parallel-projected view. This function is useful when you need an absolute zoom factor for a parallel-projected view.
    """,

    "syntax_html": """
        Rhino.ViewRadius ([strView [, dblRadius]])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "Radius",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The view radius.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblRadius is not specified, the current view radius for the specified view if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblRadius is specified, the previous view radius for the specified view if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 824,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

