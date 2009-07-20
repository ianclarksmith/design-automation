a_tan_h = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "a_tan_h",

    "doc_html": """
        Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is number; ATanH(TanH(number)) equals number.
    """,

    "syntax_html": """
        Rhino.ATanH (dblNumber)
    """,

    "params_html": {
        0: {
            "name": "Number",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A number between -1 and 1.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The inverse hyperbolic tangent of a number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 764,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

