line_max_distance_to = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "line_max_distance_to",

    "doc_html": """
        Finds the longest distance between the line, as a finite chord, and a point or another line.
    """,

    "syntax_html": """
        Rhino.LineMaxDistanceTo (arrLine, arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Line",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The test point.
            """
        },
        2: {
            "name": "Line2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        Two 3-D points identifying the starting and ending points of the test line (another finite chord).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P)."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 901,

    "params_com": {
        0: {
            "name": "vaLine",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

