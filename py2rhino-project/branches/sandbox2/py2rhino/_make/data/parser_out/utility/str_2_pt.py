str_2_pt = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "Str2Pt",
    "output_package_name": "utility",
    "output_module_name": "str_2_pt",

    "doc_html": """
        Converts a formatted string value into a 3-D point value.
    """,

    "syntax_html": {
        0: ("strPoint"),
    },

    "params_html": {
        0: {
            "name": "strPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Point",
            "doc": """
        A string that contains a delimited point like "1,2,3".
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 409,

    "params_com": {
        0: {
            "name": "vaStr",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

