sort_numbers = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SortNumbers",
    "output_package_name": "utility",
    "output_module_name": "sort_numbers",

    "doc_html": """
        Sorts an array of numbers.
    """,

    "syntax_html": {
        0: ("arrNumbers", "blnAscending"),
    },

    "params_html": {
        0: {
            "name": "arrNumbers",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Numbers",
            "doc": """
        An array of numeric values.
            """
        },
        1: {
            "name": "blnAscending",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Ascending",
            "doc": """
        The sorting mode, either ascending or descending.  If omitted, the numbers are sorted ascending.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of sorted numbers if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 552,

    "params_com": {
        0: {
            "name": "vaNumbers",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAscending",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

