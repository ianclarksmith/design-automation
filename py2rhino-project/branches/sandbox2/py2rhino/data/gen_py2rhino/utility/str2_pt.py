str2_pt = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "Str2Pt",
    "output_package_name": "utility",
    "output_module_name": "str2_pt",

    "doc_html": """
        Converts a formatted string value into a 3-D point value.
    """,

    "syntax_html": """
        Rhino.Str2Pt (strPoint)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

