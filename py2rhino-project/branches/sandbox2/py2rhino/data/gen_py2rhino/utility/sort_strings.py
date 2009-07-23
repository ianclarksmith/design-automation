sort_strings = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SortStrings",
    "output_package_name": "utility",
    "output_module_name": "sort_strings",

    "doc_html": """
        Sorts an array of strings.
    """,

    "syntax_html": {
        0: ("arrStrings", "blnAscending", "blnNoCase"),
    },

    "params_html": {
        0: {
            "name": "arrStrings",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Strings",
            "doc": """
        An array of string values.
            """
        },
        1: {
            "name": "blnAscending",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Ascending",
            "doc": """
        The sorting mode, either ascending or descending.  If omitted or True, the strings are sorted ascending.  If False, the strings are sorted descending.
            """
        },
        2: {
            "name": "blnNoCase",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "NoCase",
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

