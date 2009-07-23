ellipse_quad_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "EllipseQuadPoints",
    "output_package_name": "curve",
    "output_module_name": "ellipse_quad_points",

    "doc_html": """
        Returns the quadrant points of an elliptical-shaped curve object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points identifying the quadrants of the ellipse if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 525,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

