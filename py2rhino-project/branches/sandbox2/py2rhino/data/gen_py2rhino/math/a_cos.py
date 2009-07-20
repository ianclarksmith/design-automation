a_cos = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "a_cos",

    "doc_html": """
        Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to PI.
    """,

    "syntax_html": """
        Rhino.ACos (dblNumber)
    """,

    "params_html": {
        0: {
            "name": "Number",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A number representing the cosine of the angle you want and must be from -1 to 1.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "An angle, ?, measured in radians, such that 0 = ? = PI. Use ToDegrees to convert from radians to degrees."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 757,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

