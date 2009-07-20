point_transform = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointTransform",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_transform",

    "doc_html": """
        Transforms a 3-D point.
    """,

    "syntax_html": """
        Rhino.PointTransform (arrPoint, arrXform)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point to transform.
            """
        },
        1: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A valid 4x4 transformation matrix.
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

    "id_com": 671,

    "params_com": {
        0: {
            "name": "vaPt",
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

