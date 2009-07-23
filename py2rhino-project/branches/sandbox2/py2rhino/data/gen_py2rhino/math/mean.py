mean = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Mean",
    "output_package_name": "math",
    "output_module_name": "mean",

    "doc_html": """
        Returns the mean number, or average, from an array of numbers.
    """,

    "syntax_html": {
        0: ("arrNumbers"),
    },

    "params_html": {
        0: {
            "name": "arrNumbers",
            "py_name": "numbers",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Numbers",
            "doc": """
        An array of numbers to analyze.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The mean number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 771,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

