a_tan2 = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "a_tan2",

    "doc_html": """
        Returns the angle whose tangent is the quotient of two specified numbers.
    """,

    "syntax_html": """
        Rhino.ATan2 (dblNumberY, dblNumberX)
    """,

    "params_html": {
        0: {
            "name": "NumberY",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The y coordinate of a point.
            """
        },
        1: {
            "name": "NumberX",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The x coordinate of a point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "An angle, ?, measured in radians, such that -PI = ? = PI, and Tan(?) = y / x, where (x, y) is a point in the Cartesian plane."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 758,

    "params_com": {
        0: {
            "name": "vy",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

