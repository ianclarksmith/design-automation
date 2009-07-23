add_ellipse3_pt = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddEllipse3Pt",
    "output_package_name": "curve",
    "output_module_name": "add_ellipse3_pt",

    "doc_html": """
        Adds a 3 point elliptical curve to the document.
    """,

    "syntax_html": {
        0: ("arrCenter", "arrSecond", "arrThird"),
    },

    "params_html": {
        0: {
            "name": "arrCenter",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Center",
            "doc": """
        The center point of the ellipse.
            """
        },
        1: {
            "name": "arrSecond",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Second",
            "doc": """
        The end point of the X-axis.
            """
        },
        2: {
            "name": "arrThird",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Third",
            "doc": """
        The end point of the Y-axis.
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

    "id_com": 680,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSecond",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaThird",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

