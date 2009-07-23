get_points = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPoints",
    "output_package_name": "user_interface",
    "output_module_name": "get_points",

    "doc_html": """
        Pauses for user input of one or more points.
    """,

    "syntax_html": {
        0: ("blnDraw", "blnPlane", "strMessage1", "strMessage2", "intMaxPoints", "arrBasePoint"),
    },

    "params_html": {
        0: {
            "name": "blnDraw",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Draw",
            "doc": """
        Draw lines between points.  The default is not to draw lines between points (False).
            """
        },
        1: {
            "name": "blnPlane",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Plane",
            "doc": """
        Constrain the point selection to the active construction plane.  The default is not to constrain points to the active construction plane (False).
            """
        },
        2: {
            "name": "strMessage1",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message1",
            "doc": """
        A prompt or message for the first point.
            """
        },
        3: {
            "name": "strMessage2",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message2",
            "doc": """
        A prompt or message for the next points.
            """
        },
        4: {
            "name": "intMaxPoints",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "MaxPoints",
            "doc": """
        The maximum number of points to pick.  If not specified, an unlimited number of points can be picked.
            """
        },
        5: {
            "name": "arrBasePoint",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "BasePoint",
            "doc": """
        A starting, or base, point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 67,

    "params_com": {
        0: {
            "name": "vaDraw",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPrompt1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPrompt2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaMax",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaBase",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

