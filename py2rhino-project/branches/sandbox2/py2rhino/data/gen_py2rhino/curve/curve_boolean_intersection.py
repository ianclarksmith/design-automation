curve_boolean_intersection = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveBooleanIntersection",
    "output_package_name": "curve",
    "output_module_name": "curve_boolean_intersection",

    "doc_html": """
        Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    """,

    "syntax_html": {
        0: ("strCurveA", "strCurveB"),
    },

    "params_html": {
        0: {
            "name": "strCurveA",
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

    "id_com": 810,

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

