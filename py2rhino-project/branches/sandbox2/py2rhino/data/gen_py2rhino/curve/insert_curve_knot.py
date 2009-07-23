insert_curve_knot = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "InsertCurveKnot",
    "output_package_name": "curve",
    "output_module_name": "insert_curve_knot",

    "doc_html": """
        Inserts a knot into a curve object.
    """,

    "syntax_html": {
        0: ("strObject", "dblParameter", "blnSymmetrical"),
    },

    "params_html": {
        0: {
            "name": "strObject",
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
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Parameter",
            "doc": """
        The parameter on the curve.
            """
        },
        2: {
            "name": "blnSymmetrical",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Symmetrical",
            "doc": """
        If blnSymmetrical = True, then knots are added on both sides of the center of the curve. The default value is False.
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

    "id_com": 515,

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
        2: {
            "name": "vaSym",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

