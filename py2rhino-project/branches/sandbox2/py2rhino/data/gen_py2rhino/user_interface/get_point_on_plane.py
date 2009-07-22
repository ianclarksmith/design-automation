get_point_on_plane = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPointOnPlane",
    "output_package_name": "user_interface",
    "output_module_name": "get_point_on_plane",

    "doc_html": """
        Pauses for user input of a point constrained to a plane.
    """,

    "syntax_html": """
        Rhino.GetPointOnPlane (strMessage, arrPlane [, arrPoint])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The plane to constrain the point to.
            """
        },
        2: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A 3-D point from with to draw a tracking line. If omitted, a tracking line will not be drawn.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point selected by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 797,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

