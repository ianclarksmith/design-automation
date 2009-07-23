a_tan2 = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ATan2",
    "output_package_name": "math",
    "output_module_name": "a_tan2",

    "doc_html": """
        Returns the angle whose tangent is the quotient of two specified numbers.
    """,

    "syntax_html": {
        0: ("dblNumberY", "dblNumberX"),
    },

    "params_html": {
        0: {
            "name": "dblNumberY",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "NumberY",
            "doc": """
        The y coordinate of a point.
            """
        },
        1: {
            "name": "dblNumberX",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "NumberX",
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

