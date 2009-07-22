xform_planar_projection = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformPlanarProjection",
    "output_package_name": "transformation",
    "output_module_name": "xform_planar_projection",

    "doc_html": """
        Returns a transformation matrix that projects to a plane.
    """,

    "syntax_html": """
        Rhino.XformPlanarProjection (arrPlane)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

