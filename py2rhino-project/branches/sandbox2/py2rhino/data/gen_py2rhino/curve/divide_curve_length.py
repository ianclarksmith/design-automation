divide_curve_length = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "DivideCurveLength",
    "output_package_name": "curve",
    "output_module_name": "divide_curve_length",

    "doc_html": """
        Divides a curve object into segments of a specified length.
    """,

    "syntax_html": {
        0: ("strObject", "dblLength", "blnCreate", "blnPoints"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "dblLength",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The length of each segment.
            """
        },
        2: {
            "name": "blnCreate",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Create",
            "doc": """
        Create the division points. If omitted or False, points are not created.
            """
        },
        3: {
            "name": "blnPoints",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Points",
            "doc": """
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnPoints is not specified or True, then an array containing 3-D division points if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnPoints is False, then an array containing division curve parameters if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 374,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLength",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCreate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPoints",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

