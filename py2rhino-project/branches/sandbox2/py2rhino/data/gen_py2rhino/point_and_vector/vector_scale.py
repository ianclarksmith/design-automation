vector_scale = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorScale",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_scale",

    "doc_html": """
        Scales a 3-D vector.
    """,

    "syntax_html": {
        0: ("arrVector", "dblScale"),
    },

    "params_html": {
        0: {
            "name": "arrVector",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector",
            "doc": """
        The 3-D vector to scale.
            """
        },
        1: {
            "name": "dblScale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The scale factor to apply.
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

    "id_com": 619,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

