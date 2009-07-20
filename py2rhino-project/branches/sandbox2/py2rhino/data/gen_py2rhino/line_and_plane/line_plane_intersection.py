line_plane_intersection = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "line_plane_intersection",

    "doc_html": """
        Calculates the intersection of a line and a plane.
    """,

    "syntax_html": """
        Rhino.LinePlaneIntersection (arrLine, arrPlane)
    """,

    "params_html": {
        0: {
            "name": "Line",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line to intersect.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane to intersect.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point of intersection is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 743,

    "params_com": {
        0: {
            "name": "vaLine",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

