curve_arc_length_point = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveArcLengthPoint",
    "output_package_name": "curve",
    "output_module_name": "curve_arc_length_point",

    "doc_html": """
        Returns the point on the curve that is a specified arc length from the start of the curve.
    """,

    "syntax_html": {
        0: ("strObject", "dblLength", "blnFromStart"),
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
            "name": "dblLength",
            "py_name": "length",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The arc length from the start of the curve to evaluate.
            """
        },
        2: {
            "name": "blnFromStart",
            "py_name": "from_start",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "FromStart",
            "doc": """
        If not specified or True, then the arc length point is calculated from the start of the curve. If False, the arc length point is calculated from the end of the curve.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 658,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLength",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaStart",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

