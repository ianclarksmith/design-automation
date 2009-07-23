extend_curve_point = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ExtendCurvePoint",
    "output_package_name": "curve",
    "output_module_name": "extend_curve_point",

    "doc_html": """
        Extends a non-closed curve object by smooth extension to a point.
    """,

    "syntax_html": {
        0: ("strObject", "intSide", "arrPoint"),
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
            "name": "intSide",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Side",
            "doc": """
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
            """
        },
        2: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the extended object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 437,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSize",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

