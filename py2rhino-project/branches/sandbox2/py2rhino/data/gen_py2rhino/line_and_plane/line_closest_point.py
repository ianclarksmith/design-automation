line_closest_point = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "line_closest_point",

    "doc_html": """
        Finds the point on an infinite line that is closest to a test point.
    """,

    "syntax_html": """
        Rhino.LineClosestPoint (arrLine, arrPoint)
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The point on the line that is closest to the test point is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 899,

    "params_com": {
        0: {
            "name": "vaLine",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

