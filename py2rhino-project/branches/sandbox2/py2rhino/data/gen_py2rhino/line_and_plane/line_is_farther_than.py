line_is_farther_than = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineIsFartherThan",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_is_farther_than",

    "doc_html": """
        Determines if the shortest distance from a line to a point or another line is greater than a specified distance.
    """,

    "syntax_html": {
        0: ("arrLine", "dblDistance", "arrPoint"),
        1: ("arrLine", "dblDistance", "arrLine2"),
    },

    "params_html": {
        0: {
            "name": "arrLine",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Line",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line.
            """
        },
        1: {
            "name": "dblDistance",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        The distance.
            """
        },
        2: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Point",
            "doc": """
        The test point.
            """
        },
        3: {
            "name": "arrLine2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Line2",
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

