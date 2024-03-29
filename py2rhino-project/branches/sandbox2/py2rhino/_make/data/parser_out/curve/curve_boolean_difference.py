curve_boolean_difference = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveBooleanDifference",
    "output_package_name": "curve",
    "output_module_name": "curve_boolean_difference",

    "doc_html": """
        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    """,

    "syntax_html": {
        0: ("strCurveA", "strCurveB"),
    },

    "params_html": {
        0: {
            "name": "strCurveA",
            "py_name": "curve_a",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "CurveA",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "strCurveB",
            "py_name": "curve_b",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "CurveB",
            "doc": """
        The identifier of the second curve object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 811,

    "params_com": {
        0: {
            "name": "vaCurveA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurveB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

