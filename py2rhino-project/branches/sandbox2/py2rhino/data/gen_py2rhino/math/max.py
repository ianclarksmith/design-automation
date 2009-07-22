max = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Max",
    "output_package_name": "math",
    "output_module_name": "max",

    "doc_html": """
        Returns the maximum number from an array of numbers.
    """,

    "syntax_html": """
        Rhino.Max (arrNumbers)
    """,

    "params_html": {
        0: {
            "name": "Numbers",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_int",
            "doc": """
        An array of numbers to analyze.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The maximum number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 768,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

