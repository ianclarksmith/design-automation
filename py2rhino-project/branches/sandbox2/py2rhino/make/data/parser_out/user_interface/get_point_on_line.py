get_point_on_line = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPointOnLine",
    "output_package_name": "user_interface",
    "output_module_name": "get_point_on_line",

    "doc_html": """
        Pauses for user input of a point constrained to an infinite line.
    """,

    "syntax_html": {
        0: ("strMessage", "arrStart", "arrEnd", "blnTrack"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "arrStart",
            "py_name": "start",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Start",
            "doc": """
        The starting point of the line.
            """
        },
        2: {
            "name": "arrEnd",
            "py_name": "end",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "End",
            "doc": """
        The ending point of the line.
            """
        },
        3: {
            "name": "blnTrack",
            "py_name": "track",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Track",
            "doc": """
        Draw a tracking line from arrStart. If omitted, a tracking line is drawn (True).
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

    "id_com": 798,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaTracking",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

