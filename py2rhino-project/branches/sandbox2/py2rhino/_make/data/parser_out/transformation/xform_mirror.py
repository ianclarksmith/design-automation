xform_mirror = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformMirror",
    "output_package_name": "transformation",
    "output_module_name": "xform_mirror",

    "doc_html": """
        Creates a mirror transformation matrix.
    """,

    "syntax_html": {
        0: ("arrPoint", "arrNormal"),
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
        A 3-D point on mirror plane.
            """
        },
        1: {
            "name": "arrNormal",
            "py_name": "normal",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Normal",
            "doc": """
        A 3-D vector that is normal to mirror plane.
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

    "id_com": 795,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNormal",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

