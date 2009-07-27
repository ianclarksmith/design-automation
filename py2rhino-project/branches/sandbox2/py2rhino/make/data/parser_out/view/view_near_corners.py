view_near_corners = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewNearCorners",
    "output_package_name": "view",
    "output_module_name": "view_near_corners",

    "doc_html": """
        Returns the 3-D corners points of a view's near clipping plane rectangle. This function can be useful in determining the "real world" size of a parallel-projected view.
    """,

    "syntax_html": {
        0: ("strView"),
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of four 3-D points that define the corners of the rectangle if successful.  Points are returned in counter-clockwise order."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 823,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

