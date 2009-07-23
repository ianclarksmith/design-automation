line_min_distance_to = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineMinDistanceTo",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_min_distance_to",

    "doc_html": """
        Finds the shortest distance between the line, as a finite chord, and a point or another line.
    """,

    "syntax_html": {
        0: ("arrLine", "arrPoint"),
        1: ("arrLine", "arrLine2"),
    },

    "params_html": {
        0: {
            "name": "arrLine",
            "py_name": "line",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Line",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line.
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Point",
            "doc": """
        The test point.
            """
        },
        2: {
            "name": "arrLine2",
            "py_name": "line2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Line2",
            "doc": """
        Two 3-D points identifying the starting and ending points of the test line (another finite chord).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P)."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 900,

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

