log10 = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Log10",
    "output_package_name": "math",
    "output_module_name": "log10",

    "doc_html": """
        Returns the base-10 logarithm of a number.
    """,

    "syntax_html": """
        Rhino.Log10 (dblNumber)
    """,

    "params_html": {
        0: {
            "name": "Number",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The positive real number for which you want the base-10 logarithm.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The base-10 logarithm of the number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 777,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

