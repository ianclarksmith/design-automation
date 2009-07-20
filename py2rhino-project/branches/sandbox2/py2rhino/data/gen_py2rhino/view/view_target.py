view_target = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewTarget",
    "output_package_name": "view",
    "output_module_name": "view_target",

    "doc_html": """
        Returns or sets the target location of the specified view.
    """,

    "syntax_html": """
        Rhino.ViewTarget ([strView [, arrTarget]])
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
            "name": "Target",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point identifying the new target location.  If arrTarget is not specified, the current target location is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrTarget is not specified,  then a 3-D point containing the current target location if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrTarget is specified,  then a 3-D point containing the previous target location if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 395,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTarget",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

