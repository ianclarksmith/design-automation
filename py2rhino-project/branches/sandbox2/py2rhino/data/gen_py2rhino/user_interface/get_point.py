get_point = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_point",

    "doc_html": """
        Pauses for user input of a point.
    """,

    "syntax_html": """
        Rhino.GetPoint ([strMessage [, arrPoint [, dblDistance [, blnPlane]]]])
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
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying a starting, or base, point.
            """
        },
        2: {
            "name": "Distance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A constraining distance.  If a constraining distance is specified, a base point must also be specified.
            """
        },
        3: {
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Constrain the point selection to the active construction plane.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array containing three numbers identifying the 3-D point input by the user successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 61,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDistance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

