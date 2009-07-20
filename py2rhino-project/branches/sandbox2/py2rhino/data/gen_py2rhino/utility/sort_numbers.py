sort_numbers = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "sort_numbers",

    "doc_html": """
        Sorts an array of numbers.
    """,

    "syntax_html": """
        Rhino.SortNumbers (arrNumbers [, blnAscending])
    """,

    "params_html": {
        0: {
            "name": "Numbers",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of numeric values.
            """
        },
        1: {
            "name": "Ascending",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

