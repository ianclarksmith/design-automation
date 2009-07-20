close_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CloseCurve",
    "output_package_name": "curve",
    "output_module_name": "close_curve",

    "doc_html": """
        Closes an open curve object by making adjustments to the end points so that they meet at a point.
    """,

    "syntax_html": """
        Rhino.CloseCurve (strObject [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the closed curve object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 440,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

