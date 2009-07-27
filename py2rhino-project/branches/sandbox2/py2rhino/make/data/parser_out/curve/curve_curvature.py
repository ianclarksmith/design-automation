curve_curvature = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveCurvature",
    "output_package_name": "curve",
    "output_module_name": "curve_curvature",

    "doc_html": """
        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.
    """,

    "syntax_html": {
        0: ("strObject", "dblParameter"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "dblParameter",
            "py_name": "parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Parameter",
            "doc": """
        The parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of curvature information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "Radius of curvature"
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 379,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

