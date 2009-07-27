curve_evaluate = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveEvaluate",
    "output_package_name": "curve",
    "output_module_name": "curve_evaluate",

    "doc_html": """
        A general purpose curve evaluator.
    """,

    "syntax_html": {
        0: ("strObject", "dblParameter", "intDerivative"),
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
        The evaluation parameter.
            """
        },
        2: {
            "name": "intDerivative",
            "py_name": "derivative",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Derivative",
            "doc": """
        The number of derivatives to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of length (intDerivative+1) if successful.  The array elements are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The 3-D point"
        },
        2: {
            "type": "array",
            "doc": "The first derivative"
        },
        3: {
            "type": "array",
            "doc": "The second derivative"
        },
        4: {
            "type": "array",
            "doc": "etc..."
        },
        5: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 489,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDevCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

