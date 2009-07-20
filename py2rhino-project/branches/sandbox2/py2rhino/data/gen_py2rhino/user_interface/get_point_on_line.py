get_point_on_line = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_point_on_line",

    "doc_html": """
        Pauses for user input of a point constrained to an infinite line.
    """,

    "syntax_html": """
        Rhino.GetPointOnLine (strMessage, arrStart, arrEnd [, blnTrack])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "Start",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The starting point of the line.
            """
        },
        2: {
            "name": "End",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The ending point of the line.
            """
        },
        3: {
            "name": "Track",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

