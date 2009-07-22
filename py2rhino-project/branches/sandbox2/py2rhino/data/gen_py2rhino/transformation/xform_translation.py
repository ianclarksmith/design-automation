xform_translation = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformTranslation",
    "output_package_name": "transformation",
    "output_module_name": "xform_translation",

    "doc_html": """
        Creates a translation transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformTranslation (arrVector)
    """,

    "params_html": {
        0: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

