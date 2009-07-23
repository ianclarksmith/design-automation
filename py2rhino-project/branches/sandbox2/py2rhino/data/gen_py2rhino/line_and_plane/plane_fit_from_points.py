plane_fit_from_points = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneFitFromPoints",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_fit_from_points",

    "doc_html": """
        Returns a plane that was fit through an array of 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoints"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 725,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

