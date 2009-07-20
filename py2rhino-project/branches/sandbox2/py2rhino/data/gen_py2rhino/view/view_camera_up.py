view_camera_up = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewCameraUp",
    "output_package_name": "view",
    "output_module_name": "view_camera_up",

    "doc_html": """
        Returns or sets the camera up direction of specified view.
    """,

    "syntax_html": """
        Rhino.ViewCameraUp ([strView [, arrUpVector]])
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
            "name": "UpVector",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D vector identifying the new camera location.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrUpVector is not specified,  then a 3-D vector identifying the current camera up direction if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrUpVector is specified,  then a 3-D vector identifying the previous camera up direction if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 517,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaUp",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

