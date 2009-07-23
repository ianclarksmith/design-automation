sum = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Sum",
    "output_package_name": "math",
    "output_module_name": "sum",

    "doc_html": """
        Returns the sum of an array of numbers.
    """,

    "syntax_html": {
        0: ("arrNumbers"),
    },

    "params_html": {
        0: {
            "name": "arrNumbers",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Numbers",
            "doc": """
        An array of numbers to sum.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The sum of the array if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 770,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

