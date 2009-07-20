str2_pt_array = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "str2_pt_array",

    "doc_html": """
        Converts a formatted string value into an array of 3-D point value.
    """,

    "syntax_html": """
        Rhino.Str2PtArray (strPoints)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A string that contains an unknown number of space delimited points like "1,2,3 4,5,6 7,8,9".
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 410,

    "params_com": {
        0: {
            "name": "vaStr",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

