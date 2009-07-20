plane_plane_intersection = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "plane_plane_intersection",

    "doc_html": """
        Calculates the intersection of two planes.
    """,

    "syntax_html": """
        Rhino.PlanePlaneIntersection (arrPlane1, arrPoint2)
    """,

    "params_html": {
        0: {
            "name": "Plane1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first plane to intersect.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second plane to intersect.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "Two 3-D points identifying the starting and ending points of the intersection line."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 744,

    "params_com": {
        0: {
            "name": "vaPlaneA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlaneB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

