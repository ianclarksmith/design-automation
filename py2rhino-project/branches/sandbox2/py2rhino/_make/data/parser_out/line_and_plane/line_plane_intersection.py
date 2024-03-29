line_plane_intersection = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LinePlaneIntersection",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_plane_intersection",

    "doc_html": """
        Calculates the intersection of a line and a plane.
    """,

    "syntax_html": {
        0: ("arrLine", "arrPlane"),
    },

    "params_html": {
        0: {
            "name": "arrLine",
            "py_name": "line",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Line",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line to intersect.
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
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

