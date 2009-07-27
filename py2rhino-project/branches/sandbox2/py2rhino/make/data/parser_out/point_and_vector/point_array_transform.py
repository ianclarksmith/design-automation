point_array_transform = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointArrayTransform",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_array_transform",

    "doc_html": """
        Transforms an array of 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoints", "arrXform"),
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
        An array of 3-D points to transform.
            """
        },
        1: {
            "name": "arrXform",
            "py_name": "xform",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xform",
            "doc": """
        A valid 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 802,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

