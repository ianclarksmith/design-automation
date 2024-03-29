line_closest_point = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineClosestPoint",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_closest_point",

    "doc_html": """
        Finds the point on an infinite line that is closest to a test point.
    """,

    "syntax_html": {
        0: ("arrLine", "arrPoint"),
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
        Two 3-D points identifying the starting and ending points of the line.
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

