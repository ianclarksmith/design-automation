view_c_plane = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_c_plane",

    "doc_html": """
        Returns or sets the specified view's construction plane.
    """,

    "syntax_html": """
        Rhino.ViewCPlane ([strView [, arrPlane]])
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
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The new construction plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If a construction plane is not specified, the current construction plane if successful."
        },
        1: {
            "type": "array",
            "doc": "If a construction plane is specified, the previous construction plane if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 264,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

