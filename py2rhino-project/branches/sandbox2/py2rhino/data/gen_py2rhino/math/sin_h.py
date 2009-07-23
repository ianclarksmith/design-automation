sin_h = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "SinH",
    "output_package_name": "math",
    "output_module_name": "sin_h",

    "doc_html": """
        Returns the hyperbolic sine of the specified angle.
    """,

    "syntax_html": {
        0: ("dblAngle"),
    },

    "params_html": {
        0: {
            "name": "dblAngle",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        An angle, measured in radians.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The hyperbolic sine of dblAngle if successful. Use ToDegrees to convert from radians to degrees."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 759,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

