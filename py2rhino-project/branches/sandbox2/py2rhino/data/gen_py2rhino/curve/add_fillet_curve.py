add_fillet_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddFilletCurve",
    "output_package_name": "curve",
    "output_module_name": "add_fillet_curve",

    "doc_html": """
        Adds a fillet curve between two curve objects.
    """,

    "syntax_html": """
        Rhino.AddFilletCurve (strCurve0, strCurve1 [, dblRadius [, arrBasePoint0 [, arrBasePoint1]]])
    """,

    "params_html": {
        0: {
            "name": "Curve0",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "Curve1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the second curve object.
            """
        },
        2: {
            "name": "Radius",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The fillet radius. If omitted, a radius of 1.0 is specified.
            """
        },
        3: {
            "name": "Point0",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The base point on the first curve. If omitted, the starting point of the curve is used.
            """
        },
        4: {
            "name": "Point1",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The base point on the second curve. If omitted, the starting point of the curve is used.
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

    "id_com": 574,

    "params_com": {
        0: {
            "name": "vaCrv0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrv1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRadius",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPt0",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaPt1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

