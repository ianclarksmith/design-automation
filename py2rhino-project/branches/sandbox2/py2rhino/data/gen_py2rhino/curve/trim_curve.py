trim_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "TrimCurve",
    "output_package_name": "curve",
    "output_module_name": "trim_curve",

    "doc_html": """
        Trims a curve by removing portions of the curve outside the specified interval.
    """,

    "syntax_html": """
        Rhino.TrimCurve (strObject , arrInterval [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Interval",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete the input curve. The default is to delete the input curve (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the newly created curve object, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 505,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaInterval",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

