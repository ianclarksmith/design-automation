rotate_camera = {
    "input_folder_name": "View_Methods",
    "input_file_name": "RotateCamera",
    "output_package_name": "view",
    "output_module_name": "rotate_camera",

    "doc_html": """
        Rotates a perspective-projected view's camera. See the RotateCamera command in the Rhino help file for more details.
    """,

    "syntax_html": """
        Rhino.RotateCamera ([strview [, intDirection [, dblAngle]]])
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
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Number, The direction to rotate the camera where 0 = right, 1 = left, 2 = down, and 3 = up",
            "type_string": "int",
            "doc": """
        The default is 0 = right.
            """
        },
        2: {
            "name": "Angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle to rotate. If omitted, the angle of rotation is specified by the "Increment in divisions of a circle" parameter specified in Options command's View tab.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 519,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAngle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

