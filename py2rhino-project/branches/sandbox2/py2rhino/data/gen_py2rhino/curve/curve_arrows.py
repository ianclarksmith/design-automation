curve_arrows = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveArrows",
    "output_package_name": "curve",
    "output_module_name": "curve_arrows",

    "doc_html": """
        Enables or disabled a curve object's annotation arrows.
    """,

    "syntax_html": {
        0: ("strObject", "intStyle"),
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
            "name": "intStyle",
            "py_name": "style",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Style",
            "doc": """
        The style of annotation arrows to be displayed.  The styles are as follows:
		Value
		Description
		0
		No annotation arrows
		1
		Display an annotation arrow at the starting point of the curve
		2
		Display an annotation arrow at the ending point of the curve
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intStyle is not specified, the current annotation arrow style if successful."
        },
        1: {
            "type": "number",
            "doc": "If intStyle is specified, the previous annotation arrow style if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 578,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

