is_curve_linear = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "IsCurveLinear",
    "output_package_name": "curve",
    "output_module_name": "is_curve_linear",

    "doc_html": """
        Verifies an object is a linear curve object.
    """,

    "syntax_html": {
        0: ("strObject", "intIndex"),
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
            "name": "intIndex",
            "py_name": "index",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Index",
            "doc": """
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 105,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

