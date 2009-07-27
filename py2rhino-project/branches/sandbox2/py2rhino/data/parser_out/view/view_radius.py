view_radius = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewRadius",
    "output_package_name": "view",
    "output_module_name": "view_radius",

    "doc_html": """
        Returns or sets the radius of the viewing frustum of a parallel-projected view. This function is useful when you need an absolute zoom factor for a parallel-projected view.
    """,

    "syntax_html": {
        0: ("strView", "dblRadius"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "dblRadius",
            "py_name": "radius",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
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

