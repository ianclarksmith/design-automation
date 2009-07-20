view_camera_target = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_camera_target",

    "doc_html": """
        Returns or sets the camera and target positions of the specified view.
    """,

    "syntax_html": """
        Rhino.ViewCameraTarget ([strView [, arrCamera [, arrTarget]]])
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
        A 3-D point identifying the new camera location.  If both arrCamera and arrTarget are not specified, the current camera and target locations are returned.
            """
        },
        2: {
            "name": "Target",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point identifying the new target location.  If both arrCamera and arrTarget are not specified, the current camera and target locations are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If both arrCamera and arrTarget are not specified,  then an array of 3-D point containing the current camera and target locations is returned."
        },
        1: {
            "type": "array",
            "doc": "If either arrCamera or arrTarget are specified,  then an array of 3-D point containing the previous camera and target locations is returned."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 263,

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
        2: {
            "name": "vaTarget",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

