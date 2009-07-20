sort_strings = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SortStrings",
    "output_package_name": "utility",
    "output_module_name": "sort_strings",

    "doc_html": """
        Sorts an array of strings.
    """,

    "syntax_html": """
        Rhino.SortStrings (arrStrings [, blnAscending [, blnNoCase]])
    """,

    "params_html": {
        0: {
            "name": "Strings",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of string values.
            """
        },
        1: {
            "name": "Ascending",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The sorting mode, either ascending or descending.  If omitted or True, the strings are sorted ascending.  If False, the strings are sorted descending.
            """
        },
        2: {
            "name": "NoCase",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The case sensitivity mode.  If omitted or True, a case insensitive sorting is performed.  If False, a case sensitive sorting is performed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array sorted strings if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 640,

    "params_com": {
        0: {
            "name": "vaStrings",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaNoCase",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

