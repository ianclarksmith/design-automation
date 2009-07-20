view_camera_plane = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_camera_plane",

    "doc_html": """
        Returns the orientation of a view's camera.
    """,

    "syntax_html": """
        Rhino.ViewCameraPlane ([strView])
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The view's camera plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 778,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

