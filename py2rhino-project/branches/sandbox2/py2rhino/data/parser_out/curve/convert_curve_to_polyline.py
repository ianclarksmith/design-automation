convert_curve_to_polyline = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ConvertCurveToPolyline",
    "output_package_name": "curve",
    "output_module_name": "convert_curve_to_polyline",

    "doc_html": """
        Converts a curve to a polyline curve.
    """,

    "syntax_html": {
        0: ("strObject", "dblAngleTolerance", "dblTolerance", "blnDeleteInput"),
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
            "name": "dblAngleTolerance",
            "py_name": "angle_tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "AngleTolerance",
            "doc": """
        The maximum angle between curve tangents at line endpoints.  If omitted, the angle tolerance is set to 5.0.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the tolerance is set to 0.01.
            """
        },
        3: {
            "name": "blnDeleteInput",
            "py_name": "delete_input",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "DeleteInput",
            "doc": """
        Delete the curve object specified by strObject.  If omitted, strObject will not be deleted.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 377,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLineAngleTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaLineTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

