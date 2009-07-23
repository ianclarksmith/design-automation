a_cos_h = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ACosH",
    "output_package_name": "math",
    "output_module_name": "a_cos_h",

    "doc_html": """
        Returns the inverse hyperbolic cosine of a number. Number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is number, so ACosH(CosH(number)) equals the number.
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
        A number equal to or greater than 1.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The inverse hyperbolic cosine of a number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 763,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

