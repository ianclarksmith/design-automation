add_arc_3_pt = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddArc3Pt",
    "output_package_name": "curve",
    "output_module_name": "add_arc_3_pt",

    "doc_html": """
        Adds a 3-point arc curve to the document.
    """,

    "syntax_html": {
        0: ("arrStart", "arrEnd", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "arrStart",
            "py_name": "start",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Start",
            "doc": """
        The starting point of the arc.
            """
        },
        1: {
            "name": "arrEnd",
            "py_name": "end",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "End",
            "doc": """
        The ending point of the arc.
            """
        },
        2: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A point on the arc.
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

    "id_com": 82,

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

