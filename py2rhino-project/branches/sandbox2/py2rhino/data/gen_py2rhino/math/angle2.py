angle2 = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Angle2",
    "output_package_name": "math",
    "output_module_name": "angle2",

    "doc_html": """
        Measures the angle between two lines.
    """,

    "syntax_html": """
        Rhino.Angle2 (arrLine1, arrLine2)
    """,

    "params_html": {
        0: {
            "name": "Point1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array containing the starting and ending 3-D points of the first line.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array containing the starting and ending 3-D points of the second line.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the following elements if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 116,

    "params_com": {
        0: {
            "name": "vaFirst",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSecond",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

