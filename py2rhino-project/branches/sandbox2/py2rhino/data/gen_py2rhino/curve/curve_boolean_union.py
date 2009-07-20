curve_boolean_union = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveBooleanUnion",
    "output_package_name": "curve",
    "output_module_name": "curve_boolean_union",

    "doc_html": """
        Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    """,

    "syntax_html": """
        Rhino.CurveBooleanUnion (arrCurves)
    """,

    "params_html": {
        0: {
            "name": "Curves",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of two or more curve objects.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 809,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

