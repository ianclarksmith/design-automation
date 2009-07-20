hypot = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Hypot",
    "output_package_name": "math",
    "output_module_name": "hypot",

    "doc_html": """
        Calculates the length of the hypotenuse of a right triangle, given the length of the two sides x and y (in other words, the square root of x2 + y2).
    """,

    "syntax_html": """
        Rhino.Hypot (dblNumberX, dblNumberY)
    """,

    "params_html": {
        0: {
            "name": "NumberX",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The x value.
            """
        },
        1: {
            "name": "NumberY",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The y value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The length of the hypotenuse if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 765,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vy",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

