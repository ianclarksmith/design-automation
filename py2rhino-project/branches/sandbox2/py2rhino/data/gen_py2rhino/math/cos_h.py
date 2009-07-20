cos_h = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "CosH",
    "output_package_name": "math",
    "output_module_name": "cos_h",

    "doc_html": """
        Returns the hyperbolic cosine of the specified angle.
    """,

    "syntax_html": """
        Rhino.CosH (dblAngle)
    """,

    "params_html": {
        0: {
            "name": "Angle",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        An angle, measured in radians.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The hyperbolic cosine of dblAngle if successful. Use ToDegrees to convert from radians to degrees."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 760,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

