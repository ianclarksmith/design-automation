cull_duplicate_strings = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "cull_duplicate_strings",

    "doc_html": """
        Removes duplicates from an array of strings.
    """,

    "syntax_html": """
        Rhino.CullDuplicateStrings (arrStrings [, blnCaseSensitive)
    """,

    "params_html": {
        0: {
            "name": "Strings",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of numbers.
            """
        },
        1: {
            "name": "CaseSensitive",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Use case sensitivity when culling.  The default is to cull with case sensitivity (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings with duplicates removed if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 549,

    "params_com": {
        0: {
            "name": "vaStrings",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCaseSensitive",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

