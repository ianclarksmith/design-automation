remove_curve_knot = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "RemoveCurveKnot",
    "output_package_name": "curve",
    "output_module_name": "remove_curve_knot",

    "doc_html": """
        Deletes a knot from a curve object.
    """,

    "syntax_html": """
        Rhino.RemoveCurveKnot (strObject, dblParameter)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve object.
            """
        },
        1: {
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
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

