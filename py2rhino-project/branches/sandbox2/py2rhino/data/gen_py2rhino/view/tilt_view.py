tilt_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "TiltView",
    "output_package_name": "view",
    "output_module_name": "tilt_view",

    "doc_html": """
        Tilts a view by rotating the camera up vector.  See the TiltView command in the Rhino help file for more details.
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
            "type": "Number, The direction to rotate the camera where 0 = right and 1 = left",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        
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

    "id_com": 518,

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

