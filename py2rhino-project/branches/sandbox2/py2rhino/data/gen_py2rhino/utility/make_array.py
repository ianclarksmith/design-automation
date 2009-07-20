make_array = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "MakeArray",
    "output_package_name": "utility",
    "output_module_name": "make_array",

    "doc_html": """
        Creates a new, initialized one-dimensional array of a user-specified bounds.
    """,

    "syntax_html": """
        Rhino.MakeArray (nUpperBound [, vVariant)
    """,

    "params_html": {
        0: {
            "name": "UpperBound",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "n",
            "doc": """
        The upper bounds of the new array.
            """
        },
        1: {
            "name": "vVariant",
            "opt_or_req": "Optional",
            "type": "Variant",
            "type_string": "n",
            "doc": """
        The value to initialize every array element.  If omitted, every array element will be initialized as Empty.  Note, the Empty VBScript keyword is used to indicate an uninitialized variable value.  This is not the same thing as Null.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The one-dimensional array if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 875,

    "params_com": {
        0: {
            "name": "vaRGB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

