points_are_coplanar = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointsAreCoplanar",
    "output_package_name": "point_and_vector",
    "output_module_name": "points_are_coplanar",

    "doc_html": """
        Verifies that an array of 3-D points are co-planar.
    """,

    "syntax_html": {
        0: ("arrPoints", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.
            """
        },
        1: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        A tolerance to use when verifying. The default is to use Rhino's internal zero tolerance (1.0e-12).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating either coplanar or not coplanar, respectively, if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 593,

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

