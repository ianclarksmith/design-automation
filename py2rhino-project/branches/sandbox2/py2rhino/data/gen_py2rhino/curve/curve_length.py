curve_length = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveLength",
    "output_package_name": "curve",
    "output_module_name": "curve_length",

    "doc_html": """
        Returns the length of a curve object.
    """,

    "syntax_html": """
        Rhino.CurveLength (strObject [, intIndex [, arrSubDomain]])
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
            "name": "Index",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            """
        },
        2: {
            "name": "SubDomain",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_int",
            "doc": """
        An array of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The length of the curve if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 97,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDomain",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

