xform_translation = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformTranslation",
    "output_package_name": "transformation",
    "output_module_name": "xform_translation",

    "doc_html": """
        Creates a translation transformation matrix.
    """,

    "syntax_html": {
        0: ("arrVector"),
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
        A 3-D translation vector.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 792,

    "params_com": {
        0: {
            "name": "vaVector",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

