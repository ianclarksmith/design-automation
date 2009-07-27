remove_curve_knot = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "RemoveCurveKnot",
    "output_package_name": "curve",
    "output_module_name": "remove_curve_knot",

    "doc_html": """
        Deletes a knot from a curve object.
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
        The identifier of the curve object.
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
        The parameter on the curve.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 916,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKnot",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

