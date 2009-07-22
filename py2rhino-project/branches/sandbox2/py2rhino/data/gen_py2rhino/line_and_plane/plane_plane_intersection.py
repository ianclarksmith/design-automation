plane_plane_intersection = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlanePlaneIntersection",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_plane_intersection",

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
            "type_string": "arr_of_dbl",
            "doc": """
        The first plane to intersect.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

