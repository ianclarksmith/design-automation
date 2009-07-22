extend_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ExtendCurve",
    "output_package_name": "curve",
    "output_module_name": "extend_curve",

    "doc_html": """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.
    """,

    "syntax_html": """
        Rhino.ExtendCurve (strObject, intType, intSide, arrObjects)
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
            "name": "Type",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
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
            "name": "Side",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
            """
        },
        3: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
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

    "id_com": 438,

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
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

