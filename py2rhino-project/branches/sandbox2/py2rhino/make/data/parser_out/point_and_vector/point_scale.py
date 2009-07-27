point_scale = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointScale",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_scale",

    "doc_html": """
        Scales a 3-D point.
    """,

    "syntax_html": {
        0: ("arrPoint", "dblScale"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The 3-D point to scale.
            """
        },
        1: {
            "name": "dblScale",
            "py_name": "scale",
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
            "doc": "The resulting 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 669,

    "params_com": {
        0: {
            "name": "vaPt",
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

