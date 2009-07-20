line_is_farther_than = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "line_is_farther_than",

    "doc_html": """
        Determines if the shortest distance from a line to a point or another line is greater than a specified distance.
    """,

    "syntax_html": """
        Rhino.LineIsFartherThan (arrLine, dblDistance, arrPoint)
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
            "name": "Distance",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The distance.
            """
        },
        2: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The test point.
            """
        },
        3: {
            "name": "Line2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        Two 3-D points identifying the starting and ending points of the test line.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the shortest distance from the line to the other object is greater than dblDistance, False otherwise."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 902,

    "params_com": {
        0: {
            "name": "vaLine",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDist",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

