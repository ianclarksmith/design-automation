view_camera = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_camera",

    "doc_html": """
        Returns or sets the camera location of the specified view.
    """,

    "syntax_html": """
        Rhino.ViewCamera ([strView [, arrCamera]])
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
            "name": "Camera",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point identifying the new camera location.  If arrCamera is not specified, the current camera location is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrCamera is not specified,  then a 3-D point containing the current camera location if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrCamera is specified,  then a 3-D point containing the previous camera location if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 394,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCamera",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

