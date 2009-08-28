vector_rotate = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorRotate",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_rotate",

    "doc_html": """
        Rotates a 3-D vector.
    """,

    "syntax_html": {
        0: ("arrVector", "dblAngle", "arrAxis"),
    },

    "params_html": {
        0: {
            "name": "arrVector",
            "py_name": "vector",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector",
            "doc": """
        The 3-D vector.
            """
        },
        1: {
            "name": "dblAngle",
            "py_name": "angle",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The rotation angle in degrees.
            """
        },
        2: {
            "name": "arrAxis",
            "py_name": "axis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Axis",
            "doc": """
        A 3-D vector defining the axis of rotation.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D vector if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 678,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAngle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAxis",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

