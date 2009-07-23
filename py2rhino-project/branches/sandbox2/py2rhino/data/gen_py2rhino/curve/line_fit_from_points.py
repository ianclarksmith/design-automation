line_fit_from_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "LineFitFromPoints",
    "output_package_name": "curve",
    "output_module_name": "line_fit_from_points",

    "doc_html": """
        Returns the starting and ending points of a line that was fit through an array of 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoints"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        An array of 3-D points. The array must contain at least two 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the starting and ending points of the fit line if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 726,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

