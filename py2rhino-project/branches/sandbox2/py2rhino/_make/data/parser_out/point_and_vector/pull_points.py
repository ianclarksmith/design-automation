pull_points = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PullPoints",
    "output_package_name": "point_and_vector",
    "output_module_name": "pull_points",

    "doc_html": """
        Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoints"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the surface or mesh object that pulls.
            """
        },
        1: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points to pull.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 716,

    "params_com": {
        0: {
            "name": "vaObject",
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

