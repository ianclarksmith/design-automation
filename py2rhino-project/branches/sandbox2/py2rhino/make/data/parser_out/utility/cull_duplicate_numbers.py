cull_duplicate_numbers = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "CullDuplicateNumbers",
    "output_package_name": "utility",
    "output_module_name": "cull_duplicate_numbers",

    "doc_html": """
        Removes duplicates from an array of numbers.
    """,

    "syntax_html": {
        0: ("arrNumbers", "dblTolerance"),
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
        An array of numbers.
            """
        },
        1: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The minimum distance between numbers.  Numbers that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of numbers with duplicates removed if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 550,

    "params_com": {
        0: {
            "name": "vaNumbers",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

