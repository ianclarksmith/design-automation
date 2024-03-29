curve_deviation = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveDeviation",
    "output_package_name": "curve",
    "output_module_name": "curve_deviation",

    "doc_html": """
        Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.
    """,

    "syntax_html": {
        0: ("strCurveA", "strCurveB"),
    },

    "params_html": {
        0: {
            "name": "strCurveA",
            "py_name": "curve_a",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "CurveA",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "strCurveB",
            "py_name": "curve_b",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "CurveB",
            "doc": """
        The identifier of the second curve object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of numbers identifying the minimum and maximum deviation between the two curves if successful."
        },
        1: {
            "type": "number",
            "doc": "Curve A parameter at maximum overlap distance point"
        },
        2: {
            "type": "number",
            "doc": "Curve A parameter at maximum overlap distance point"
        },
        3: {
            "type": "number",
            "doc": "Maximum overlap distance"
        },
        4: {
            "type": "number",
            "doc": "Curve A parameter at minimum distance point"
        },
        5: {
            "type": "number",
            "doc": "Curve B parameter at minimum distance point"
        },
        6: {
            "type": "number",
            "doc": "Minimum distance between curves"
        },
        7: {
            "type": "null",
            "doc": "On error or if no intervals of overlap were found."
        },
    },

    "id_com": 687,

    "params_com": {
        0: {
            "name": "vaCrvA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrvB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

