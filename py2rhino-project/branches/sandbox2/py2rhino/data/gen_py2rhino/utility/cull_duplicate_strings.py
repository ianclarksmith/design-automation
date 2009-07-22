cull_duplicate_strings = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "CullDuplicateStrings",
    "output_package_name": "utility",
    "output_module_name": "cull_duplicate_strings",

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
            "type_string": "arr_of_int",
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

