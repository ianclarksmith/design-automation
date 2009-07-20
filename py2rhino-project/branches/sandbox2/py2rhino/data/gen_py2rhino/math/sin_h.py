sin_h = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "sin_h",

    "doc_html": """
        Returns the hyperbolic sine of the specified angle.
    """,

    "syntax_html": """
        Rhino.SinH (dblAngle)
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

