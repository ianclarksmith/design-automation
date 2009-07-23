add_circle3_pt = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddCircle3Pt",
    "output_package_name": "curve",
    "output_module_name": "add_circle3_pt",

    "doc_html": """
        Adds a 3-point circle curve to the document.
    """,

    "syntax_html": {
        0: ("arrFirst", "arrSecond", "arrThird"),
    },

    "params_html": {
        0: {
            "name": "arrFirst",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "First",
            "doc": """
        The first point of the circle.
            """
        },
        1: {
            "name": "arrSecond",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Second",
            "doc": """
        The second point of the circle.
            """
        },
        2: {
            "name": "arrThird",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Third",
            "doc": """
        The third point of the circle.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 84,

    "params_com": {
        0: {
            "name": "vaPt1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPt3",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

