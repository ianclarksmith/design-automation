curve_seam = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveSeam",
    "output_package_name": "curve",
    "output_module_name": "curve_seam",

    "doc_html": """
        Adjusts the seam, or start/end, point of a closed curve.
    """,

    "syntax_html": """
        Rhino.CurveSeam (strObject, dblParameter)
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
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The parameter of the new start/end point. Note, if successful, the resulting curve's domain will start at dblParameter.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 527,

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
    },

    "returns_com": "tagVARIANT",

}

