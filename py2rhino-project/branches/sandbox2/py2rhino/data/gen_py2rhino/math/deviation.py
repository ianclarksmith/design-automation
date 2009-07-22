deviation = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Deviation",
    "output_package_name": "math",
    "output_module_name": "deviation",

    "doc_html": """
        Returns the standard deviation from an array of numbers.
    """,

    "syntax_html": """
        Rhino.Deviation (arrNumbers)
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
            "doc": "The standard deviation if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 773,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

