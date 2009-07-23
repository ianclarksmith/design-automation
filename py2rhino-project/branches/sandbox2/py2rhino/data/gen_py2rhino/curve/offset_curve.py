offset_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "OffsetCurve",
    "output_package_name": "curve",
    "output_module_name": "offset_curve",

    "doc_html": """
        Offsets a curve by a distance. The offset curve will be added to Rhino.
    """,

    "syntax_html": {
        0: ("strObject", "arrDirection", "dblDistance", "arrNormal", "intStyle"),
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
            "name": "arrDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Direction",
            "doc": """
        The 3-D point that indicates the direction of the offset.
            """
        },
        2: {
            "name": "dblDistance",
            "py_name": "distance",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        The distance of the offset.
            """
        },
        3: {
            "name": "arrNormal",
            "py_name": "normal",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Normal",
            "doc": """
        A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
            """
        },
        4: {
            "name": "intStyle",
            "py_name": "style",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Style",
            "doc": """
        The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the new objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 634,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDistance",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaNormal",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaCorner",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

