cull_duplicate_numbers = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "cull_duplicate_numbers",

    "doc_html": """
        Removes duplicates from an array of numbers.
    """,

    "syntax_html": """
        Rhino.CullDuplicateNumbers (arrNumbers [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Numbers",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of numbers.
            """
        },
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

