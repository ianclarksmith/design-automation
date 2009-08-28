xform_planar_projection = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformPlanarProjection",
    "output_package_name": "transformation",
    "output_module_name": "xform_planar_projection",

    "doc_html": """
        Returns a transformation matrix that projects to a plane.
    """,

    "syntax_html": {
        0: ("arrPlane"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The plane to project to.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 793,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

