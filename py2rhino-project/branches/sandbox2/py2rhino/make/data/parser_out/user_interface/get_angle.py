get_angle = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetAngle",
    "output_package_name": "user_interface",
    "output_module_name": "get_angle",

    "doc_html": """
        Pauses for user input of an angle.
    """,

    "syntax_html": {
        0: ("arrPoint", "arrReference", "dblAngle", "strMessage"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying the starting, or base, point.
            """
        },
        1: {
            "name": "arrReference",
            "py_name": "reference",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Reference",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying a reference point.  If specified, the reference angle is calculated from it and the base point.
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
        A default angle value specified in degrees.
            """
        },
        3: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The angle in degrees if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 277,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRef",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDefault",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

