extend_curve_length = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ExtendCurveLength",
    "output_package_name": "curve",
    "output_module_name": "extend_curve_length",

    "doc_html": """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.
    """,

    "syntax_html": {
        0: ("strObject", "intType", "intSide", "dblLength"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "intType",
            "py_name": "type",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Type",
            "doc": """
        Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
            """
        },
        2: {
            "name": "intSide",
            "py_name": "side",
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
		Extend from the end of the curve.
		2
            """
        },
        3: {
            "name": "dblLength",
            "py_name": "length",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The distance to extend the curve.
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

    "id_com": 436,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaType",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSide",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaLength",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

