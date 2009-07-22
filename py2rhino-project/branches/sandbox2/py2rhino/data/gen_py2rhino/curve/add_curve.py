add_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddCurve",
    "output_package_name": "curve",
    "output_module_name": "add_curve",

    "doc_html": """
        Adds a control points curve object to the document.
    """,

    "syntax_html": """
        Rhino.AddCurve (arrPoints [, intDegree])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array of 3-D points.
            """
        },
        1: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The degree of the curve.  If omitted, a degree 3 curve is created.
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

    "id_com": 77,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

