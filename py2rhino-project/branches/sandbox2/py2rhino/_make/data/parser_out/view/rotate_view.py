rotate_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "RotateView",
    "output_package_name": "view",
    "output_module_name": "rotate_view",

    "doc_html": """
        Rotates a view. See the RotateView command in the Rhino help file for more information.
    """,

    "syntax_html": {
        0: ("strview", "intDirection", "dblAngle"),
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
            "name": "intDirection",
            "py_name": "direction",
            "opt_or_req": "Optional",
            "type": "Number, The direction to rotate the view, where 0 = right, 1 = left, 2 = down, and 3 = up",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The default is 0 = right.
            """
        },
        2: {
            "name": "dblAngle",
            "py_name": "angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
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

    "id_com": 650,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAngle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

