curve_edit_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveEditPoints",
    "output_package_name": "curve",
    "output_module_name": "curve_edit_points",

    "doc_html": """
        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.
    """,

    "syntax_html": {
        0: ("strObject", "blnReturnParameters", "intIndex"),
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
            "name": "blnReturnParameters",
            "py_name": "return_parameters",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnParameters",
            "doc": """
        Return the edit points as an array of parameter values.  If omitted, the edit points are returned as an array of 3-D points.
            """
        },
        2: {
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
            "type": "array",
            "doc": "If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnReturnParameters is True, then an array of parameter values if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 442,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReturnParameters",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

