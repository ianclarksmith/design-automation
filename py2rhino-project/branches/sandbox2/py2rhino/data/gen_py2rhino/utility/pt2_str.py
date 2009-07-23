pt2_str = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "Pt2Str",
    "output_package_name": "utility",
    "output_module_name": "pt2_str",

    "doc_html": """
        Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.
    """,

    "syntax_html": {
        0: ("arrPoint", "nPrecision", "blnSpace"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point.
            """
        },
        1: {
            "name": "nPrecision",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "n",
            "name_main": "Precision",
            "doc": """
        The display precision of the point coordinates.  The default is to display the precision defined by the display precision setting that is found on the Units page of the DocumentProperties command.
            """
        },
        2: {
            "name": "blnSpace",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Space",
            "doc": """
        Append an additional trailing space after the point string.  The default value is not to append the additional space (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The formatted string if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 297,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrecision",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSpace",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

