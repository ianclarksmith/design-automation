a_sin_h = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ASinH",
    "output_package_name": "math",
    "output_module_name": "a_sin_h",

    "doc_html": """
        Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is number, so ASinH(SinH(number)) equals number.
    """,

    "syntax_html": {
        0: ("dblNumber"),
    },

    "params_html": {
        0: {
            "name": "dblNumber",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Number",
            "doc": """
        Any real number.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The inverse hyperbolic sine of a number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 762,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

