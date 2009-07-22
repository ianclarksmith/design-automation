add_line = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddLine",
    "output_package_name": "curve",
    "output_module_name": "add_line",

    "doc_html": """
        Adds a line curve to the current model.
    """,

    "syntax_html": """
        Rhino.AddLine (arrStart, arrEnd)
    """,

    "params_html": {
        0: {
            "name": "Start",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The starting point of the line.
            """
        },
        1: {
            "name": "End",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The ending point of the line.
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

    "id_com": 70,

    "params_com": {
        0: {
            "name": "vaPoint1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

