reverse_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ReverseCurve",
    "output_package_name": "curve",
    "output_module_name": "reverse_curve",

    "doc_html": """
        Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.
    """,

    "syntax_html": """
        Rhino.ReverseCurve (strObject)
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

    "id_com": 542,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

