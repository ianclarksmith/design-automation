strtok = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "Strtok",
    "output_package_name": "utility",
    "output_module_name": "strtok",

    "doc_html": """
        Returns the tokens in a string.  Use this method as an alternative to the VBScript's Split function.
    """,

    "syntax_html": {
        0: ("strText", "strDelimiters"),
    },

    "params_html": {
        0: {
            "name": "strText",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        A string containing token(s).
            """
        },
        1: {
            "name": "strDelimiters",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Delimiters",
            "doc": """
        A set of delimiter characters.  If omitted, a space character (" ") is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array containing the string tokens if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 250,

    "params_com": {
        0: {
            "name": "vaString",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSeps",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

