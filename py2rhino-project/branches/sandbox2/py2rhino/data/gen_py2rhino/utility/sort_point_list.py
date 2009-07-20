sort_point_list = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SortPointList",
    "output_package_name": "utility",
    "output_module_name": "sort_point_list",

    "doc_html": """
        Sorts an array of 3-D points so they will be connected in "reasonable" polyline order.
    """,

    "syntax_html": """
        Rhino.SortPointList (arrPoints [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.
            """
        },
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The minimum distance between points.  Points that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of sorted 3-D points  if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 644,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

