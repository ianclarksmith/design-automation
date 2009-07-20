get_points = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_points",

    "doc_html": """
        Pauses for user input of one or more points.
    """,

    "syntax_html": """
        Rhino.GetPoints ([blnDraw [, blnPlane [, strMessage1 [, strMessage2 [, intMaxPoints [, arrBasePoint]]]]]])
    """,

    "params_html": {
        0: {
            "name": "Draw",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Draw lines between points.  The default is not to draw lines between points (False).
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Constrain the point selection to the active construction plane.  The default is not to constrain points to the active construction plane (False).
            """
        },
        2: {
            "name": "Message1",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message for the first point.
            """
        },
        3: {
            "name": "Message2",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message for the next points.
            """
        },
        4: {
            "name": "MaxPoints",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The maximum number of points to pick.  If not specified, an unlimited number of points can be picked.
            """
        },
        5: {
            "name": "BasePoint",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
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

