get_angle = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetAngle",
    "output_package_name": "user_interface",
    "output_module_name": "get_angle",

    "doc_html": """
        Pauses for user input of an angle.
    """,

    "syntax_html": """
        Rhino.GetAngle (arrPoint, arrReference, dblAngle, strMessage)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying the starting, or base, point.
            """
        },
        1: {
            "name": "Reference",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying a reference point.  If specified, the reference angle is calculated from it and the base point.
            """
        },
        2: {
            "name": "Angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A default angle value specified in degrees.
            """
        },
        3: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

